# Task 0 — Repo Setup

Purpose: Bootstrap the repository for vibe-centric workflows and align docs, sessions, and tasks.

## Testing

- Open `.continue/config.json` and confirm context providers include `.github`, `docs/guides`, `tasks/templates`, `sessions`, and top-level `README.md`, `TASKS.md` (or replacement).
- Render `.github/chatmodes/*.md` and check links.
- Lint markdown spacing for chatmodes (MD022/MD032) on changed files.

## Step Table

| Step | Status | Description |
|------|--------|-------------|
| 1 | TODO | Move root `TASKS.md` into `tasks/` as `task-0-repo-setup.md`. |
| 2 | TODO | Create `tasks/tasks.md` index with Testing-first section. |
| 3 | TODO | Update `README.md` references from `TASKS.md` to `tasks/tasks.md`. |
| 4 | TODO | Create/verify `sessions/dev-sessions.md` from stub and log first entry. |
| 5 | OPTIONAL | Run repo-wide markdownlint and fix spacing issues. |

## Working State (Agent Handoff)

<!-- TASK:WORKING-STATE:BEGIN -->
- Current focus: migrate tasks to `tasks/` dir, keep minimal diffs.
- Assumptions: no existing `tasks/tasks.md`; will create.
- Next action: add `tasks/tasks.md` index; replace root `TASKS.md` with pointer.
<!-- TASK:WORKING-STATE:END -->

## Context & Notes

- Follow `.github/copilot-instructions.md` for mode triggers and quality gates.
- Use append-only anchors for session logs per `dev-session-mode.md`.
