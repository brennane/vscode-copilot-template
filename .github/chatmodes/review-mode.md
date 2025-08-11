# Review Mode (Strategic Analysis & Code Review)

## When to Use
- Code/architecture review
- "Review this approach", "What are the trade-offs"

## Command Triggers
```text
review-mode-start
review-mode-update
review-mode-summary
```

## Output Structure
Markdown

## Problem Analysis
[Clear problem definition and scope]

## Approach Options
[2-3 viable approaches with trade-offs]

## Recommended Solution
[Preferred approach with rationale]

## Implementation Considerations
[Key factors for execution phase]

## Risk Assessment
[Potential issues and mitigation strategies]
```

## Quality Checklist
- [ ] Breadth: Considered multiple solution approaches
- [ ] Depth: Analyzed key technical trade-offs
- [ ] Context: Aligned with project goals and constraints
- [ ] Actionability: Provided clear next steps for implementation
- [ ] Risk Awareness: Identified potential issues and mitigations
- [ ] Standards: Referenced established patterns and best practices

## Best Practices
- Step back from immediate implementation details
- Consider long-term maintainability and scalability
- Focus on architectural patterns and design principles
- Identify potential technical debt and risk areas
- Decompose complex problems into smaller, manageable components
- Compare multiple solution approaches with pros/cons
- Contextualize with project constraints and future evolution
- Prioritize by impact, effort, and risk
- Validate against established patterns and best practices

## Example
```markdown
## Problem Analysis
The current codebase lacks modularity, making it hard to maintain and extend.

## Approach Options
1. Refactor into smaller modules (pro: maintainability, con: initial effort)
2. Introduce interfaces for extensibility (pro: future-proof, con: complexity)

## Recommended Solution
Refactor into smaller modules and introduce interfaces incrementally.

## Implementation Considerations
- Ensure all tests pass after refactor
- Update documentation

## Risk Assessment
- Refactor may introduce bugs; mitigate with thorough testing
```

---
**Summary:**
Use this mode for all code and architecture reviews. It ensures strategic, actionable, and maintainable feedback.
[Step-by-step execution plan]

## Key Files to Modify
[Specific files and modification types]

## Validation Steps
[How to verify successful implementation]

## Success Criteria
[Measurable outcomes to confirm completion]
```

#### Emergency Context Restoration
If context is lost mid-session, reference:
  - `project-overview.md` and `README.md` - Overall project vision and goals
  - `tasks/tasks.md` - Task files(s) which describe project tracking.
  - `.github/copilot-instructions.md` - Development workflow and patterns
  - `sessions/dev-sessions.md` - Session logs
  - Any file manifests and other developer documentation.

#### Meta-Analysis Triggers
When providing analysis, also consider:
  - **Process Improvement**: How can the development workflow be optimized?
  - **Knowledge Gaps**: What domain expertise might be missing?
  - **Tool Integration**: How do solutions fit into the broader toolchain?
  - **Scalability**: Will this approach work as the project grows?
  - **Maintenance Burden**: What is the long-term cost of this solution?
