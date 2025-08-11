# LLM Mode - Working with AI Agents

## When to Use
Expert help when dealing with Copilot Agent, other coding agents, LLM prompting, and workflows.

## Command Triggers
- `llm-mode`
- `llm-mode cache`
- `llm-mode prompt ...`
- "Build an LLM Prompt to do a thing."
- "Help me evaluate the AI Agent workflow for such and thus."

## Core Competencies

### 🗂️ **File & Directory Organization**

- **Semantic categorization** over alphabetical sorting
- **Purpose-driven directory structure** design
- **Clean separation** of concerns (tests vs test-drivers, docs vs tasks, etc.)
- **VSCode workspace optimization** for developer experience

### 🔧 **Git & Version Control Excellence**

- **Branch strategy** recommendations
- **Commit message** standardization
- **File movement** with proper git history preservation
- **.gitignore** optimization

### 📋 **Documentation Hygiene**

- **Pointer document** maintenance and updates
- **Cross-reference** validation and repair
- **Stale file** identification and cleanup
- **README hierarchy** organization

### 🤖 **Agent-Optimized Structure**

- **Context caching** for efficient AI workflows
- **Semantic file naming** for improved discoverability
- **State preservation** for multi-session work
- **Working context** compression and storage

## Specialized Commands

### `llm-mode cache`

**Purpose**: Create compressed agent state cache for efficient context loading

**Output**: `CACHE.md` with:

- **Timestamp** and relevance indicators
- **Current work summary** (1-2 sentences)
- **Key file pointers** (5-10 most relevant files with purpose)
- **Working state** (active tasks, blockers, next steps)
- **Context shortcuts** (command snippets, test procedures)
- **Technical context** (architecture decisions, feature breakdowns)
- **Expiration logic** (conditions when cache becomes stale)

**Template:**

````markdown
# Agent Cache - [YYYY-MM-DD HH:MM]

## Current State
[2-3 sentence summary of active work]

## Key Files
- **Primary**: `path/to/main/file.py` - Core functionality
- **Config**: `config/main.yaml` - Current settings
- **Tasks**: `tasks/current.md` - Active work items
- **Tests**: `tests/integration/` - Validation procedures

## Working Context
**Last Achievement**: [Specific completed milestone]
**Next Step**: [Specific actionable item]
**Blockers**: [Any impediments or dependencies]

## Quick Commands

```bash
# Install and validate
./venv/bin/pip install -e .
python -m pytest tests/integration/
```

## Cache Status
**Created**: [timestamp]
**Expires**: When [specific condition]
**Remove if**: [staleness indicators]
````

## Prompting Best Practices

### **Crafting Effective Prompts**

- **Be Specific**: Clearly define the task or question. Avoid vague or overly broad instructions.
- **Provide Context**: Include relevant background information or examples to guide the agent.
- **Iterate**: Start with a simple prompt and refine based on the agent's responses.
- **Use Constraints**: Specify output format, length, or style to ensure useful results.
- **Test Variations**: Experiment with different phrasings to find the most effective prompt.

### **Examples**

- **Task-Oriented**: "Summarize the following text in 100 words."
- **Code Generation**: "Write a Python function to calculate the factorial of a number."
- **Debugging**: "Explain why this code snippet throws an error and suggest a fix."

## Prompt Patterns and Templates

Use these lightweight templates to speed up accurate, reproducible interactions. Adapt minimally to your task.

### General Task Template

- Role: You are an expert assistant for this repository.
- Goal: State the exact outcome in one sentence.
- Inputs: List concrete files, data, or constraints.
- Output: Specify format (Markdown first; code/tests if applicable).
- Acceptance: Bullet the success criteria and edge cases.

Example:

```markdown
Role: Expert Python assistant for this repo
Goal: Implement X and update docs
Inputs: files A/B, constraints C, non-goals D
Output: Markdown summary + code edits; add tests if behavior changes
Acceptance: Lint clean; passes tests; docs updated; no GPL deps
```

### Code Change in Repo

- Name the files to edit and where in the file to work.
- Provide a tiny “contract” (inputs, outputs, error modes).
- Ask for minimally invasive diffs and tests.

Example:

```markdown
Make a minimal change in `src/foo.py`: add parse_config(path) -> dict[str, Any].
Contract: on missing file -> FileNotFoundError; on invalid -> ValueError.
Add tests in `tests/test_config.md` (driver-based). Keep public API stable.
```

### Documentation/Guides

- Provide audience and scope.
- Require concise, skimmable sections with examples.

Example:

```markdown
Audience: new contributors. Scope: run tests + generate CACHE.md.
Deliver: short guide in `docs/guides/getting-started.md` with copyable commands.
```

### Extraction/Structuring

- Specify schema and required fields.
- Provide 1-2 annotated examples and a counterexample.

Example:

```markdown
Extract IOC indicators to Markdown table with columns: type, value, source, confidence.
Include only explicit indicators; exclude inferred.
```

## Additional Best Practices for AI Workflows

### **Context Management**

- **Chunk Information**: Break large inputs into smaller, manageable pieces.
- **Use Memory Wisely**: Leverage context caching to maintain continuity across sessions.
- **Avoid Overloading**: Limit the amount of information provided in a single prompt.

### **Iterative Refinement**

- **Feedback Loop**: Review the agent's output and provide constructive feedback for improvement.
- **Layered Prompts**: Build on previous responses to refine the output incrementally.
- **Error Handling**: Identify and address misunderstandings or inaccuracies in the agent's responses.

### **Evaluation Strategies**

- **Define Success Criteria**: Establish clear metrics for evaluating the agent's performance.
- **Compare Outputs**: Test multiple approaches and compare results for quality and relevance.
- **Document Findings**: Record successful prompts and workflows for future reference.

### **Collaboration with Agents**

- **Set Expectations**: Clearly communicate the agent's role and limitations.
- **Encourage Exploration**: Allow the agent to suggest alternative solutions or approaches.
- **Maintain Oversight**: Regularly review and validate the agent's contributions to ensure accuracy.

## Output Contract Checklist

For non-trivial tasks, require the agent to:

- State inputs/outputs, error modes, and success criteria.
- Produce Markdown first (summary, decisions, risks).
- Apply minimal diffs; preserve style and public APIs.
- Run quality gates: Build, Lint/Typecheck, Tests, and a small smoke test.
- Report PASS/FAIL per gate with deltas only.
- Note any new dependencies and licenses; avoid GPL/AGPL; suggest alternatives if found.

## Context Pack (include with your prompt)

Include only what’s needed:

- Goal and non-goals (1-2 bullets each).
- Key files with one-line purpose and links/paths.
- Constraints: performance, compatibility, security, licensing.
- Quality gates to run, and which tests matter.
- Edge cases to consider (empty/null, timeouts, large inputs, auth).

## Cache Lifecycle and Use

- Create/update CACHE.md via `llm-mode cache` when starting a task or after major changes.
- Expires when files/structure shift or tasks change materially.
- Keep 5–10 key pointers max; prune aggressively to reduce noise.
- See `docs/guides/cache-task-snippet.md` for a reusable snippet and checklist.

## Mode Selection Tips

- Use llm-mode: prompting, agent workflows, caches, prompt templates.
- Use repo-mode: file organization, git ops, repo cleanup.
- Use task-mode: plan work, maintain TASKS.md, stepwise execution.
- Use doc-mode: write/refine docs and READMEs.

## Safety, Compliance, and Security

- No secrets: never request or include tokens, keys, or credentials.
- Licensing: prefer MIT/Apache; flag GPL/AGPL immediately with alternatives.
- Determinism: prefer reproducible steps and pinned deps; avoid ad-hoc installs.
- Provenance: cite files/paths for all code changes; no unverified external code.

---

**Remember**: Effective use of AI agents requires a balance of clear instructions, iterative refinement, and thoughtful evaluation. By following these best practices, you can maximize the value of AI workflows while minimizing errors and inefficiencies.
