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
Respond using structured Markdown, with focused language and bullet points.

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

Respond using structured Markdown, with focused language and bullet points.

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

## Template-Specific Guidance: Vibe-Centric Coding

- Align with `.github/copilot-instructions.md` for agent workflow, output contracts, and quality gates.
- Use chatmodes in `.github/chatmodes/` by triggers; keep outputs structured per mode.
- Maintain append-only anchors in `sessions/dev-sessions.md`; keep per-task Working State inside the task file.
- Use llm-mode cache to produce `CACHE.md` per `docs/guides/cache-task-snippet.md`.
- Ensure `.continue/config.json` includes focused context providers and a strict system message.

### Repository Template Health

- [ ] Key files present: `README.md`, `TASKS.md`, `LICENSE`, `.continue/config.json`, `.github/` chatmodes
- [ ] `TASKS.md` starts with Testing section and uses step table
- [ ] `sessions/dev-sessions.md` initialized (or `.stub` checked in)
- [ ] Links valid (README points to `docs/guides/vibe-centric-flow.md`)
- [ ] No markdownlint spacing errors in chatmodes

### Handoff Protocol (for reviewers)

Include these in your review output:

- Implementation Plan: steps and owners
- Key Files to Modify: paths and change types
- Validation Steps: how to verify success
- Success Criteria: measurable outcomes

### Emergency Context Restoration

If context is lost mid-session, reference:

- `TASKS.md` and `tasks/` for current work state
- `sessions/dev-sessions.md` for recent decisions
- `.github/copilot-instructions.md` and chatmodes for process
- `.continue/config.json` for agent context config
