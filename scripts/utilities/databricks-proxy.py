from fastapi import FastAPI, Request
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
import configparser
import os
import httpx
import argparse
import logging
import uvicorn

# https://localhost:{port}/v1/{MODEL}/complettions
# https://{WORKSPACE}/serving-endpoints/{MODEL}/invocations
# https://docs.databricks.com/aws/en/machine-learning/model-serving/structured-outputs

# Costs : In/Out Costs in DBUs per 1 million tokens
# https://www.databricks.com/product/pricing/foundation-model-serving (pricing sheet)
# https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models
# https://www.databricks.com/product/pricing/foundation-model-serving (costs)
# https://ciscotap-talos.cloud.databricks.com/ml/endpoints (for costs)
MODELS = [
    # Newer -> Older
    "databricks-gpt-oss-120b",                 # GPT OSS 120B           Cost: 42.857/214.286 (Est.)
    "databricks-gpt-oss-20b",                  # GPT OSS 20B            Cost: 42.857/214.286 (Est.)
    "databricks-llama-4-maverick",             # Llama 4 Maverick       Cost: 7.143/21.429
    "databricks-claude-sonnet-4",              # Claude Sonnet 4        Cost: 42.857/214.286
    "databricks-claude-3-7-sonnet",            # Claude 3.7 Sonnet      Cost: 42.857/214.286
    "databricks-gemma-3-12b",                  # Gemma 3.12B            Cost: 2.143/7.143
    "databricks-meta-llama-3-3-70b-instruct",  # Llama 3.3 70B Instruct Cost: 7.143/21.429 
    "databricks-meta-llama-3-1-8b-instruct",   # Llama 3.1 8B Instruct  Cost: 2.143/6.429
    "databricks-gte-large-en",                 # GTE Large (En)         Cost: 1.857/na
    "databricks-bge-large-en",                 # BAIE Large (En)        Cost: 1.429/na
]

def read_databricks_config(section="DEFAULT"):
    """
    Reads Databricks configuration from the ~/.databrickscfg file or environment variables.
    """
    config = configparser.ConfigParser()
    config.read(os.path.expanduser("~/.databrickscfg"))
        api_key = os.environ.get("DATABRICKS_API_KEY")
        if api_key:
            # Workspace must still come from config file or env
            workspace = os.environ.get("DATABRICKS_HOST")
            if not workspace:
                # Try config file for host if env not set
                workspace = config.get(section, "host", fallback=None)
            return {"workspace": workspace, "api_key": api_key}
        # Fallback: config file for both
        return {
            "workspace": config.get(section, "host", fallback=None),
            "api_key": config.get(section, "token", fallback=None),
        }

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

config = read_databricks_config('DEFAULT')
API_KEY = config['api_key']
WORKSPACE = config['workspace']

# Setup argparse
parser = argparse.ArgumentParser(description="Databricks Proxy Server")
parser.add_argument("--port", type=int, default=5000, help="Port to run the proxy server on")
args = parser.parse_args()

if not API_KEY:
if not API_KEY or not WORKSPACE:
    logger.error("Databricks API key and/or host not found. Set DATABRICKS_API_KEY and DATABRICKS_HOST env vars (preferred for Docker/CI), or ensure both are present in ~/.databrickscfg (DEFAULT section).")
    raise ValueError("Databricks API key and/or host not found. Set DATABRICKS_API_KEY and DATABRICKS_HOST env vars (preferred for Docker/CI), or ensure both are present in ~/.databrickscfg (DEFAULT section).")

# Server-wide usage metrics
from threading import Lock
usage_totals = {
    'prompt_tokens': 0,
    'completion_tokens': 0,
    'total_tokens': 0
}
usage_lock = Lock()

app = FastAPI()

# Add middleware to log invalid requests
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    return response

@app.middleware("http")
async def log_all_requests(request: Request, call_next):
    logger.info(f"Received request: Method={request.method}, URL={request.url}, Headers={dict(request.headers)}")
    response = await call_next(request)
    return response

@app.post("/v1/chat/completions")
@app.post("/v1/completions")
async def proxy_completions(request: Request):
    try:
        data = await request.json()
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }
        logger.info("Received request for completions")
        logger.debug(f"Request data: {data}")
        model_name = data.get("model", "databricks-gemma-3-12b")
        databricks_endpoint = f"{WORKSPACE}/serving-endpoints/{model_name}/invocations"
        logger.info(f'USING ENDPOINT {databricks_endpoint}')

        # Streaming support
        # data['stream'] = False
        if data.get("stream", False):
            from fastapi.responses import StreamingResponse
            import re, json
            usage_pattern = re.compile(rb'"usage"\s*:\s*\{[^}]*\}')
            buffer = b""
            usage_found = False
            def extract_and_update_usage(chunk_bytes):
                nonlocal usage_found
                matches = usage_pattern.findall(chunk_bytes)
                for match in matches:
                    try:
                        # Try to parse the usage dict
                        usage_json = b'{' + match + b'}'
                        usage_obj = json.loads(usage_json.decode(errors='ignore'))
                        usage = usage_obj.get('usage')
                        if usage and not usage_found:
                            logger.info(f"[stream] Request usage: {usage}")
                            with usage_lock:
                                for k in usage_totals:
                                    usage_totals[k] += usage.get(k, 0)
                                logger.info(f"[stream] Running totals: {usage_totals}")
                            usage_found = True
                    except Exception as e:
                        logger.debug(f"[stream] Failed to parse usage from chunk: {e}")

            async def stream_response():
                nonlocal buffer
                async with httpx.AsyncClient() as client:
                    async with client.stream("POST", databricks_endpoint, json=data, headers=headers) as resp:
                        async for chunk in resp.aiter_bytes():
                            buffer += chunk
                            extract_and_update_usage(buffer)
                            yield chunk
            logger.info("Forwarding request to Databricks endpoint with streaming enabled")
            return StreamingResponse(stream_response(), media_type="application/json")
        else:
            async with httpx.AsyncClient() as client:
                response = await client.post(databricks_endpoint, json=data, headers=headers)
                response.raise_for_status()
            logger.info("Forwarded request to Databricks endpoint")
            resp_json = response.json()
            logger.debug(f"Response data: {resp_json}")
            # Log usage and update running totals
            usage = resp_json.get('usage')
            if usage:
                logger.info(f"Request usage: {usage}")
                with usage_lock:
                    for k in usage_totals:
                        usage_totals[k] += usage.get(k, 0)
                    logger.info(f"Running totals: {usage_totals}")
            return resp_json
    #except requests.exceptions.RequestException as e:
    #    logger.error(f"Error forwarding request to Databricks: {e}")
    #    return {"error": str(e)}
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {"error": str(e)}

@app.get("/{path:path}")
async def handle_unhandled_get_requests(path: str):
    logger.warning(f"Unhandled GET request received for path: {path}")
    return JSONResponse(content={"error": "Unhandled endpoint"}, status_code=404)

@app.post("/{path:path}")
async def handle_unhandled_post_requests(path: str):
    logger.warning(f"Unhandled POST request received for path: {path}")
    return JSONResponse(content={"error": "Unhandled endpoint"}, status_code=404)

if __name__ == "__main__":
    logger.info(f"Starting proxy server on port {args.port}")
    uvicorn.run(app, host="0.0.0.0", port=args.port, log_level="debug")
