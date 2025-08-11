# Agent Cache Task Snippet (for llm-mode)

Use this snippet to quickly drive creation/update of `CACHE.md` via `llm-mode cache` without modifying `TASKS.md`.

## How to Use

- Open Chat and invoke: `llm-mode cache`.
- Paste the “Context Pack” and fill in blanks below.
- Generate `CACHE.md` at repo root and commit it.

## Testing (quick)

```bash
# Optional: ensure env is ready
./venv/bin/pip install -e .
# If tests exist, run a fast subset or smoke test
# python -m pytest tests/ -q
```

## Minimal Context Pack (copy/paste)

```markdown
Goal: Create/update CACHE.md summarizing current work and key pointers.
Non-Goals: Do not change code or move files.

Key Files:
- README.md – Repo overview
- TASKS.md – Current high-level tasks (if present)
- docs/guides/cache-task-snippet.md – This guide

Constraints:
- Output MUST be Markdown (human-readable) suitable for LLM input
- Keep 5–10 key pointers max; be concise
- Include expiration logic (when cache becomes stale)

Quality Gates:
- CACHE.md renders cleanly; headings and lists well-formed
- Links/paths valid for this repo
- No secrets, no external code

Edge Cases:
- Missing TASKS.md
- Large file scatter in root
- Recent structural changes not yet captured
```

## Steps

| Step | Status | Description |
|------|--------|-------------|
| 1 | TODO | Review current work and identify 5–10 key files to link in CACHE.md. |
| 2 | TODO | Run `llm-mode cache` and generate CACHE.md using the template. |
| 3 | TODO | Verify headings, lists, and fenced code blocks pass markdown lint. |
| 4 | TODO | Sanity-check pointers/paths and expiration logic. |
| 5 | TODO | Commit `CACHE.md` with a clear message. |

## Commit Message Template

```text
chore(cache): update CACHE.md with current state, key pointers, and next steps

- Summarize active work and blockers
- Refresh key file links (<=10)
- Note cache expiration conditions
```

## Tips

- Update CACHE.md at the start/end of a work session or after material changes.
- Prune aggressively—favor clarity over completeness.
- Keep it action-oriented: last achievement, next step, blockers.

## References

- See `llm-mode.md` → “llm-mode cache” for the canonical template.
