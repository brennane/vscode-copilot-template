# Task 0 — Repo Setup

Purpose: Bootstrap the repository for vibe-centric workflows and align docs, sessions, and tasks.

## Testing

- Render `.github/copilot-instructions.md` and check links; headings/lists have proper spacing.
- Render `.github/chatmodes/*.md` and check links; headings/lists have proper spacing.
- Open `README.md` and have user confirm that it describes the project.

## Definition of Done

- `tasks/tasks.md` or `tasks/task-$num-$desc.md` exists as the index (lowest number)
- `sessions/dev-sessions.md` exists (generated from stub) and is append-only.
- Chatmodes/docs pass basic markdown spacing checks (headings/lists).

## Step Table

| Step | Status | Description |
|------|--------|-------------|
| 1 | TODO | Use project `README.md` to scaffold files for new project work. |
| 2 | TODO | Ensure `sessions/dev-sessions.md` (from stub) is in place. |
| 3 | TODO | Review project guidance to prepare suitable `tasks/task-$num-$name.md` files. |
| 4 | OPTIONAL | Run repo-wide markdownlint and fix any remaining spacing issues. |

## Working State (Agent Handoff)

<!-- TASK:WORKING-STATE-START -->
Last Achievement: YAML consolidated; telemetry off; tasks index and pointers in place.
Next Step: Optional repo-wide markdownlint pass and polish `.continue/README.md` spacing.
Key Pointers: [`.continue/config.yaml`], [`CURRENT-TASK.md`], [`.github/copilot-instructions.md`]
Notes: Root `TASKS.md` removed or pointer-only per instructions.
<!-- TASK:WORKING-STATE-END -->

## Context & Notes

- Follow `.github/copilot-instructions.md` for mode triggers and quality gates.
- Use append-only anchors for session logs per `dev-session-mode.md`.
