# Task Mode (Development Lifecycle & Session Management)

## When to Use

Use Task Mode for creating, updating, or reviewing `tasks/tasks.md` and development planning documents. This mode is ideal for:

- Task planning and breakdown
- Sprint planning and backlog grooming
- Updating or summarizing task status
- Writing or reviewing validation steps
- Session-based effort tracking for solo or small team workflows

## Command Triggers

Activate Task Mode with these command-like triggers or natural language requests:

- `task-mode-start` — Begin a new task planning or breakdown session
- `task-mode-update` — Update or add to the current tasks/tasks.md
- `task-mode-summary` — Summarize current task status and next steps
- "Plan the next sprint"
- "Break down this feature into actionable steps"
- "Update tasks/tasks.md for this project"
- "Write validation steps for these tasks"
- "Review and update task status"
- "Add sub-tasks for this step"

---

## Output Structure

Respond using this structure, with clear acceptance criteria and session-aware tracking.

### 0. Testing (Always at Top)

Provide quick, copyable validation steps for the current task.

```bash
# Example (adjust to task)
./venv/bin/pip install -e .
# python -m pytest tests/ -q
```

### 1. Definition of Done (Always at Top)

Provide explicit acceptance criteria and validation steps that define task completion:

- **Functional Requirements**: What the code must do
- **Quality Gates**: Test coverage, code review, documentation
- **Integration Requirements**: CI/CD pipeline, deployment verification
- **Validation Steps**: Manual and automated testing procedures
- **Session Tracking**: Reference to dev session logs or complexity notes

### Task Working State (Agent Handoff)

Keep a small, persistent handoff block within each `tasks/task-*.md` file so work can pause/resume reliably.

Anchors:

- `<!-- TASK:WORKING-STATE-START -->` … `<!-- TASK:WORKING-STATE-END -->`

Rules:

- Keep under ~15 lines; update at the start/end of a work session
- Link only the 3–5 most relevant files/paths
- Put quick commands in a fenced block (bash) for copy/paste

Example block:

````markdown
<!-- TASK:WORKING-STATE-START -->
Last Achievement: [Concise milestone]
Next Step: [Single, imperative action]
Blockers: [If any]
Key Pointers: [`path/to/file1`, `path/to/file2`]
Quick Commands:

```bash
# optional, fast checks only
./venv/bin/pip install -e .
# python -m pytest tests/some_path -q
```

Notes: [Assumptions/decisions or open questions]
<!-- TASK:WORKING-STATE-END -->
````

### 2. Task Breakdown & Tracking

```markdown
| Task | Status | Acceptance Criteria | Dev Session Notes |
|------|--------|-------------------|------------------|
| Specific task | TODO | Clear success criteria | Session tracking/complexity notes |
```

- **Task**: Specific, actionable work item
- **Status**: Use `BACKLOG`, `TODO`, `IN PROGRESS`, `REVIEW`, `DONE`
- **Acceptance Criteria**: Measurable definition of completion
- **Dev Session Notes**: Complexity indicators, effort tracking references, or session log IDs

### 3. Sub-Tasks (if needed)

For complex steps, add a sub-task table:

```markdown
| Sub-Step | Status | Description |
|----------|--------|-------------|
| 1.1      | TODO   | Detailed sub-action. |
```

### 4. Validation/Testing Steps

List how to verify completion for each major task or milestone.

---

## Quality Checklist

- [ ] All tasks are broken down into clear, actionable steps
- [ ] Status is up to date for each task
- [ ] Testing/validation steps are explicit and at the top
- [ ] Sub-tasks are used for complex actions
- [ ] Descriptions are concise and unambiguous
- [ ] Table formatting is correct and easy to read

---

## Best Practices

- Update the table as tasks progress.
- Break down complex work into the smallest possible, code-actionable steps (e.g., 'Refactor pipeline to aggregate tables', 'Integrate TableMerger call', 'Add test to confirm TableMerger is called').
- Prefer explicit, atomic actions over broad or vague descriptions.
- Use language that prompts Copilot to generate code, refactor, or validate output at each step.
- Add context or examples if needed, but keep lines short.
- Use the table as the primary checklist for ongoing work.
- Always start with a Testing section.

### Update Protocol (for agents and humans)

- Update the Task Working State block at session start/end (source of truth for handoff)
- Append detailed narrative in dev sessions (see dev-session-mode) rather than inside the task file
- Keep the Task Breakdown table in sync (statuses and acceptance criteria)

### Relationship to `llm-mode cache`

- Task Working State: persistent per-task context; survives across sessions; lives in the task file
- llm-mode cache: ephemeral session context; repository-level; summarized in `CACHE.md`

#### Templates

- Use `tasks/templates/task-template.md` when creating a new task file.

---

## Example

```markdown
## Definition of Done

Functional Requirements:
- Feature X implements Y behavior
- Handles edge cases A, B, C

Quality Gates:
- 90% test coverage maintained
- Code review completed
- Documentation updated

Session Notes:
- Estimated complexity: Medium (based on similar tasks)
- Reference: Dev session log 2025-07-16

| Task | Status | Acceptance Criteria | Dev Session Notes |
|------|--------|-------------------|------------------|
| Implement feature X | TODO | Passes all unit tests, handles edge cases | Medium complexity, similar to task #45 |
| Update documentation | TODO | README reflects new feature usage | Low complexity |
```

---

## Summary

Use this mode for all planning, breakdown, and review of project tasks. Always start with a Testing section and keep all steps explicit and actionable.
