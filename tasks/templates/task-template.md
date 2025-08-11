# Task: {{short_name}}

Metadata:

- ID: {{task_id}}
- Created: {{date}}
- Owner: {{owner_or_role}}
- Priority: {{priority}}
- Tags: {{tags}}

## Testing (Always at Top)

```bash
# Adjust to this task
./venv/bin/pip install -e .
# python -m pytest tests/ -q
```

## Definition of Done

Functional Requirements:

- {{what_must_be_true}}

Quality Gates:

- Build/install succeeds
- Lint/typecheck clean
- Tests pass (add at least happy path + 1 edge)
- Docs updated if behavior changes

Integration Requirements:

- CI/automation (if applicable) updated and passing

Validation Steps:

- {{validation_steps_summary}}

Session Tracking:

- Link to dev session entry if applicable

## Task Working State (Agent Handoff)

````markdown
<!-- TASK:WORKING-STATE-START -->
Last Achievement: {{concise_milestone}}
Next Step: {{single_imperative_action}}
Blockers: {{blockers_or_none}}
Key Pointers: [`path/to/file1`, `path/to/file2`]
Quick Commands:

```bash
# optional, fast checks only
./venv/bin/pip install -e .
# python -m pytest tests/scope -q
```

Notes: {{assumptions_decisions_open_questions}}
<!-- TASK:WORKING-STATE-END -->
````

## Task Breakdown & Tracking

```markdown
| Task | Status | Acceptance Criteria | Notes |
|------|--------|---------------------|-------|
| {{specific_step}} | TODO | {{measurable_success}} | {{context_or_complexity}} |
```

## Sub-Tasks (optional)

```markdown
| Sub-Step | Status | Description |
|----------|--------|-------------|
| 1.1      | TODO   | {{detail}}  |
```

## Validation/Testing Steps

- {{how_to_verify_major_steps}}

## Context & Inputs

- Source: README.md (extract key constraints, setup, and goals)
- Constraints: {{performance_compat_security_licensing}}
- Non-Goals: {{explicitly_out_of_scope}}

## References

- Files: `path/to/file`, `another/path`
- Links: {{docs_or_external_refs}}
