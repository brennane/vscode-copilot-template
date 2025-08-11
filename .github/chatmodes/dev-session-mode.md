
# Dev Session Mode (Development Session Tracking)

## When to Use

Use Dev Session Mode for managing development session logging in `sessions/dev-sessions.md`. This mode is ideal for:

- Starting, updating, or ending a dev session log
- Capturing progress, learnings, and context for each session
- Maintaining concise, structured, and actionable logs

## Command Triggers

Activate Dev Session Mode with these command-like triggers or natural language requests:

- `dev-session` — Start, Update, Note, End as appopriate.
- `dev-session-start` — Start a new development session log
- `dev-session-update` — Update progress or add notes to the current session
- `dev-session-note` — Add an ad-hoc note or insight
- `dev-session-end` — End and summarize the current session
- "Start new dev session"
- "Log session progress"
- "End current session"

---

## Output Structure

Respond using concise, scannable formats for session tracking.

### 1. Session Start Format

```markdown
### DEV-SESSION START: YYYY-MM-DD

**Context:** [Brief description of work focus]
**Goals:** [1-3 specific objectives]
**Reference:** [Related tasks/tasks.md items or files]
```

### 2. Session Update Format

```markdown
### DEV-SESSION UPDATE: YYYY-MM-DD

**Progress:** [Key accomplishments, status changes]
**Blockers:** [Any issues encountered]
**Next:** [Immediate next steps]
```

### 3. Session Note Format

```markdown
### DEV-SESSION NOTE: YYYY-MM-DD

**Context:** [Brief situational note]
**Insight:** [Key learning or decision]
```

### 4. Session End Format

```markdown
### DEV-SESSION END: YYYY-MM-DD

**Summary:** [Major accomplishments]
**Learnings:** [Key insights, what worked/didn't]
**Metrics:** [Token usage, complexity, flow state]
**Next Session:** [Prep for next work]
```

---

## Quality Checklist

- [ ] Entries are concise and scannable (avoid walls of text)
- [ ] Session goals are specific and measurable
- [ ] Progress is linked to tasks/tasks.md items where relevant
- [ ] Learnings capture actionable insights
- [ ] Timestamps and formatting are consistent
- [ ] File length is managed (archive when needed)

---

## Best Practices

### Chronological Order

- There is a brief header in the document, do not add entries in the header
- Find the `Start new entries below` line and add entries after the separator.
- Keep document chronologically oriented.

### Conciseness Guidelines

- Use bullet points over paragraphs
- Limit session summaries to 3-5 key points
- Focus on decisions and outcomes, not process details
- Keep individual entries under 10 lines when possible

### File Management

- Archive monthly to `sessions/archive/YYYY-MM-dev-sessions.md`
- Consider splitting at 1000+ lines or 50+ sessions
- Maintain chronological order (always append)
- Link to external files for detailed context

### Session Linking

- Reference tasks/tasks.md items: "Related: task-4 Step 3"
- Note file changes: "Modified: src/parser.py, tests/test_parser.py"
- Track decision points: "Decision: Using SQLite over file-based storage"

---

## Example (Concise Format)

```markdown
### DEV-SESSION START: 2025-07-16

**Context:** PDF extraction improvements (cybersecurity pipeline)
**Goals:** 
- Fix chunking logic in pdf_extract.py
- Add error handling for malformed PDFs  
- Update tests for new edge cases
**Reference:** tasks/tasks.md Step 4

### DEV-SESSION UPDATE: 2025-07-16

**Progress:**
- ✅ Fixed chunking logic, handles overlapping text blocks
- ✅ Added try/catch for PyPDF2 errors
- 🚧 Test updates in progress (2/5 complete)
**Blockers:** None
**Next:** Complete remaining test cases

### DEV-SESSION END: 2025-07-16

**Summary:** PDF chunking improvements complete, error handling added
**Learnings:** PyPDF2 edge cases require defensive coding patterns
**Metrics:** Medium token usage, high flow state
**Next Session:** Begin Markdown output validation (Step 5)
```

---

## Summary

Use this mode for all dev session tracking to maintain concise, actionable logs. Always keep entries scannable and focused on outcomes.
