# Project Review Mode (Repository & Strategic Analysis)

## When to Use
Use Project Review Mode for whole-repository, strategic, and process reviews. This mode is ideal for:
- Architecture and design health assessments
- CI/CD and development process maturity reviews
- Technical debt and modernization planning
- Dependency, security, and documentation audits
- Team productivity and workflow optimization

## Command Triggers
Activate Project Review Mode with these command-like triggers or natural language requests:
- "Review the overall project architecture"
- "Assess our CI/CD pipeline maturity"
- "Analyze technical debt across the repository"
- "Evaluate testing strategy and coverage"
- "Review dependency management and security"
- "Assess development workflow efficiency"
- "Plan modernization and technology upgrades"
- "Review code quality standards and enforcement"

---

## Output Structure
Respond using structured Mardown, with focused language and bullet points.

## Architecture Health Assessment
[Overall system design, module boundaries, dependency management]

## Development Process Maturity
[CI/CD pipeline, testing strategy, code quality gates]

## Technical Debt Analysis
[Identified debt, impact assessment, remediation roadmap]

## Modernization Opportunities
[Technology upgrades, tooling improvements, process optimizations]

## Implementation Roadmap
[Prioritized action plan with timelines and success metrics]
```

---

## Quality Checklist
- [ ] Architecture Assessment: Evaluated system design, modularity, and scalability
- [ ] CI/CD Maturity: Assessed pipeline automation, testing integration, deployment practices
- [ ] Code Quality Standards: Reviewed linting, formatting, code review processes
- [ ] Testing Strategy: Evaluated test pyramid, coverage, automation, performance testing
- [ ] Security Posture: Checked dependency scanning, secret management, access controls
- [ ] Documentation Quality: Assessed README, API docs, architecture documentation
- [ ] Dependency Management: Reviewed update policies, vulnerability scanning, license compliance
- [ ] Performance Monitoring: Evaluated observability, metrics, alerting systems

---

## Best Practices
- Use focused, actionable language and bullet points
- Prioritize architecture, process, and testing health
- Always provide a prioritized implementation roadmap
- Reference project-specific context and success criteria
- Document assumptions, risks, and improvement opportunities

---

## Example
```markdown
## Architecture Health Assessment
- Modular monorepo with clear service boundaries
- Dependency management via poetry/requirements.txt
- Some legacy modules lack clear ownership

## Development Process Maturity
- CI/CD pipeline covers build, test, deploy, but lacks rollback automation
- Code review required for all merges; linting enforced
- Test coverage at 85%, but integration tests are sparse

## Technical Debt Analysis
- Outdated dependencies in 3 modules
- Manual deployment scripts for legacy services
- No automated secret rotation

## Modernization Opportunities
- Adopt containerization for legacy modules
- Integrate automated secret management
- Expand integration test coverage

## Implementation Roadmap
1. Containerize legacy modules (Q3)
2. Migrate manual scripts to CI/CD (Q3)
3. Add secret rotation automation (Q4)
4. Expand integration tests (Q4)
```

---

## Review Framework

### 1. Architecture & Design
- System Architecture: Microservices vs monolith, service boundaries, data flow
- Design Patterns: Consistent pattern usage, architectural styles (hexagonal, clean, etc.)
- Scalability: Horizontal/vertical scaling considerations, bottleneck identification
- Resilience: Fault tolerance, circuit breakers, retry mechanisms

### 2. Development Process Maturity
- CI/CD Pipeline: Automated testing, deployment, rollback capabilities
- Code Quality Gates: Static analysis, test coverage thresholds, security scanning
- Branching Strategy: Git flow, feature flags, environment promotion
- Release Management: Semantic versioning, changelog automation, deployment strategies

### 3. Testing Excellence
- Test Pyramid: Unit, integration, e2e test distribution and effectiveness
- Test Automation: Coverage reporting, performance testing, chaos engineering
- Quality Metrics: Defect rates, test reliability, feedback loop speed
- Testing Tools: Framework selection, test data management, mock strategies

### 4. DevOps & Infrastructure
- Infrastructure as Code: Terraform, Ansible, reproducible environments
- Containerization: Docker, Kubernetes, orchestration best practices
- Monitoring & Observability: Logging, metrics, tracing, alerting
- Security Integration: DevSecOps practices, vulnerability management

---

## Project-Specific & Advanced Guidance

### Project Context: VS Code Storm Language Extension
- Domain: Language tooling, TextMate grammars, LSP features
- Architecture: Modular grammar generation with feature flags
- Methodology: Test-driven development with incremental validation
- Quality Standards: Comprehensive test coverage, gap analysis, CI/regression detection

#### Key Technical Patterns
1. Feature Flag Architecture: Modular enabling/disabling of grammar features
2. Gap Analysis Workflow: Systematic comparison between generated and reference grammars
3. Test-Driven Grammar Development: Validate every enhancement against real syntax examples
4. Hybrid Extraction: Combine automated parsing with hardcoded Storm-specific patterns

#### Success Criteria
- Feature Parity: Match all capabilities of LLM-generated reference grammar
- Quality Metrics: Line count, test coverage, real-world validation
- Automation: Regenerate grammar automatically as language evolves
- Maintainability: Clear documentation of patterns and assumptions

#### Domain Guidance
- Grammar Design: Balance parser complexity and feature completeness
- Pattern Extraction: Weigh automation vs manual pattern definition
- Testing: Prioritize real-world samples over synthetic tests
- Performance: Consider regex complexity impact on editor responsiveness
- Modularity: Design for feature-flag based enabling/disabling
- Extensibility: Plan for future language evolution
- Compatibility: Ensure cross-platform VS Code consistency
- Debugging: Include validation and gap analysis workflows
- Coverage: Feature-based test organization
- Validation Pipeline: Automated regression detection
- Sample Selection: Real-world Storm files vs synthetic examples
- Feedback Loops: Rapid iteration with immediate validation

#### Implementation Handoff Protocol
After analysis, include:
```markdown
## Implementation Plan
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
- `project-overview.md` - Overall project vision and goals
- `tasks/task-4.md` - Current task steps and success criteria
- `sessions/dev-sessions.md` - Recent session history and learnings
- `.github/copilot-instructions.md` - Development workflow and patterns

#### Meta-Analysis Triggers
When providing analysis, also consider:
- Process Improvement: How can the development workflow be optimized?
- Knowledge Gaps: What domain expertise might be missing?
- Tool Integration: How do solutions fit into the broader toolchain?
- Scalability: Will this approach work as the project grows?
- Maintenance Burden: What is the long-term cost of this solution?
