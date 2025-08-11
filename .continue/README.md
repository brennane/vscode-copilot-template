send wire to a cloud-hosted provider.  Or, I extinguish my premium credits and want to 
reason with out inhouse AI.

# Why Continue.dev?

Continue.dev is used as an alternative to GitHub Copilot when:
- You want to use self-hosted models (e.g., Ollama, local LLMs)
- You need to access enterprise/private LLMs (e.g., Databricks, internal OpenAI endpoints)
- You hit Copilot token/credit limits or want to avoid sending code to cloud providers
- You want to experiment with different agent workflows or model providers

This enables flexible, privacy-conscious, and cost-effective AI coding—especially for regulated or internal projects.

# VS Code Profiles: Copilot vs. Continue

To easily swap between Copilot and Continue.dev, use VS Code’s built-in profile system:

## 1. Create a "Copilot" Profile
- Open Command Palette: `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
- Type: `Profiles: Create Profile`
- Name it: `Copilot`
- Install/enable GitHub Copilot extension
- (Optional) Disable Continue.dev extension

## 2. Create a "Continue" Profile
- Open Command Palette: `Profiles: Create Profile`
- Name it: `Continue`
- Install/enable Continue.dev extension
- (Optional) Disable GitHub Copilot extension
- Configure `.continue/config.yaml` for your preferred model (Ollama, Databricks, etc.)

## 3. Switching Profiles
- Open Command Palette: `Profiles: Switch Profile`
- Choose `Copilot` or `Continue` as needed

## 4. Typical Use Cases
- **Copilot profile:** General coding, cloud LLMs, GitHub integration
- **Continue profile:** Internal/enterprise LLMs, self-hosted models, privacy-sensitive work, or when Copilot is unavailable

---

**Tip:** You can export/import profiles for team sharing or backup. See VS Code docs for details.

