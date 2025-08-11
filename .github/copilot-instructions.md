# Copilot Instructions
## Chatmode Guidance

This project uses several specialized chatmodes to optimize Copilot and LLM workflows. Refer to the relevant chatmode file in `.github/chatmodes/` when you see the following triggers or tasks:

| Chatmode              | When to Use / Trigger Phrases                                      | File                                 |
|-----------------------|--------------------------------------------------------------------|--------------------------------------|
| **review-mode**       | Code/architecture review, `review-mode`, `review-mode-*`, "Review this approach", "What are the trade-offs" | review-mode.md                      |
| **project-review-mode** | Whole-repo/process/strategy review, `project-review`, `project-review-mode`, `project-review-*`, "Assess repo health", "Plan a cleanup sprint" | project-review-mode.md              |
| **task-mode**         | Task planning, breakdown, or updating `TASKS.md`, `task-mode`, `task-mode-*`, "Plan next sprint", "Break down feature" | task-mode.md                        |
| **doc-mode**          | Documentation writing/review, `dock-mode`, `doc-mode-*`, "Draft a README", "Improve onboarding" | doc-mode.md                          |
| **dev-session-mode**  | Development session logging, `dev-session`, `dev-session-*`, "Log session progress" | dev-session-mode.md                 |
| **repo-mode**         | Repository organization, file cleanup, `repo-mode`, `repo-mode organize [category]`, `tidy-mode cache`, `repo-mode repo`, "Clean up repo structure", "Organize files" | repo-mode.md                        |

**Best Practice:**

**File/Directory Naming Conventions:**
- Use `sessions/dev-sessions.md` for session logs and `sessions/archive/YYYY-MM-dev-sessions.md` for archives.
- Use `tasks/tasks.md` for the main task list and `tasks/task-x.md` for individual task files.
- Use lowercase, hyphenated filenames for all new files.

When a request matches a trigger phrase or workflow above, refer to the corresponding chatmode file for detailed instructions and output structure. This ensures consistent, high-quality, and context-aware responses.

## Environment
- Use the Python `venv` in the project root.
- Always run the VS Code task "Install Editable" to install the package in editable mode before running or testing code.

## Licensing
- Prefer MIT, Apache, or other commercially friendly licenses.
- If a dependency is found to be GPL, AGPL, or paid-license, alert and recommend alternatives.
- Clearly note and alert on any GPLv3, AGPL, or other strong copyleft or paid-license dependencies.

## Project Purpose
- Prepare HTML or PDF documents for a cybersecurity pipeline.
- Convert documents to Markdown, then process with LLMs or other systems to produce structured outputs (e.g., STIX, Vertex Project storm language).

## Coding Guidelines
- Write clean, maintainable, and well-documented code.
- Prioritize readability for humans and Copilot.
- Use descriptive names and add docstrings to public functions/classes.
- Follow PEP8 style.

## Data Structure & Architecture Guidelines
**CRITICAL LESSON: Data structure design must be prioritized from day one.**
- Use typed objects (dataclasses) for structured data rather than dictionaries
- Implement validation and conversion utilities early in the project
- Plan coordinate system architecture upfront for spatial data projects
- Avoid defensive programming patterns that mask underlying design issues
- Create factory methods (e.g., `Zone.build()`) for legacy data conversion
- Implement backward compatibility properties when transitioning from dicts to typed objects

## Stub File Handling
- When creating stub files add a marker of the same name with '.stub' appended (e.g., 'foo.py.stub').
- Alert the user and ensure a step to resolve stub file is in the current task, if applicable.

## GIT
- When asked for a git commit message write a focused message to
"GIT-COMMIT-MESSAGE" in the project root.

## Output
- All processing should produce Markdown as an intermediate step.
- Intermediate Markdown must be human-readable and suitable for LLM input.
- Final outputs must be structured for cybersecurity use cases.

## Testing
- Use the `test_data/` and `tests/` directories for test inputs and evaluation scripts.
- Tests are evaluated by writing output and log files, not with pytest or other frameworks unless explicitly allowed.
- Add new test cases and expected outputs as files in these directories.
- `tests/REGRESSION_MANIFEST.yaml` coordinates tests.

## Dependencies
- Add new dependencies to the appropriate `requirements.txt` file.
- Avoid ad-hoc package installs.

## Example Output
- Intermediate: Markdown
- Final: Structured formats such as STIX or Vertex Project storm language.

## Editing Guidance
- Use clear, concise comments to explain complex logic.
- Make stepwise changes and avoid large, monolithic edits.
- Use conservative edits to existing code, ensuring compatibility with the current project structure.
- Write explicit, unambiguous instructions and avoid vague requests.
- Break down complex tasks into smaller, well-defined steps.
- Provide relevant context, examples, and expected outputs when possible.
- Review and iterate on outputs, giving targeted feedback for improvements.
- Prefer reproducible, deterministic workflows to minimize ambiguity.
- Document assumptions and edge cases to help the agent reason effectively.

## Directory Organization & Project Structure
**CRITICAL LESSON: Semantic categorization trumps alphabetical organization.**
- Watch for file scatter in root directory - organize early
- Implement semantic categorization (not alphabetical) for scripts and documentation
- Separate active tasks (`tasks/`) from documentation (`docs/`)
- Distinguish test types clearly: `tests/` (automated pytest), `scripts/test-drivers/` (interactive)
- Use directory structure: `docs/{guides,design,analysis,status}` for documentation
- Organize scripts by purpose: `scripts/{demos,training,diagnostics,utilities}`

## Recovery & Crisis Management
**LESSON: Systematic recovery beats heroic debugging efforts.**
- Use test-driven recovery for system failures (migrate tests first)
- Create PUNCHLIST.md ordering fixes by dependency complexity (least to most)
- Make minimal, surgical changes rather than sweeping refactors
- Document architectural decisions immediately during recovery
- Validate dependencies and licenses early to prevent GPL contamination


## Task Guidance

If a `TASKS.md` file exists, treat it as the authoritative source for current work. It must clearly list actionable steps, reflect the latest project state, and serve as a concise, up-to-date scratch pad for ongoing or multi-step tasks. Ensure formatting is clear and lines are short for easy reading by both humans and Copilot.

**For all planning, breakdown, and review of project tasks, use the `task-mode` chatmode for best results.**

Always start `TASKS.md` with a **Testing** section that provides explicit instructions for running or validating the current work. Include all relevant scripts, commands, or manual steps needed to verify progress.

Use a stepwise table with these columns:

| Step | Status        | Description |
|------|--------------|-------------|
| 1    | TODO         | Short, clear action item. |

- **Step**: Sequential number for each task.
- **Status**: Use `TODO`, `IN PROGRESS`, or `DONE`.
- **Description**: Concise, explicit explanation of the task, including context and intent.

### Best Practices
- Update the table as tasks progress.
- Break down complex work into small, well-defined steps.
- Avoid vague or overly broad descriptions.
- Add context or examples if needed, but keep lines short.
- Use the table as the primary checklist for ongoing work.
