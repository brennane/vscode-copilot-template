# Repo Mode - Repository Organization & Cleanup

## When to Use
Expert-level repository organization focused on file structure, git operations, git workflow optimization, and maintaining clean, navigable codebases for both humans and AI agents.

## Command Triggers
- `repo-mode`
- `repo-mode organize [category]`  
- `repo-mode cache`
- `repo-mode repo`
- Repository cleanup requests
- File organization tasks
- "Clean up the repo structure"
- "Organize documentation"
- "Move files to proper locations"

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

### `repo-mode repo`

**Purpose** As expert in GIT version control assist in reconiling working
state of tree with vcs state.  Wait for user instructions.

### `repo-mode organize [category]`

**Categories:**
- `docs` - Move documents to proper semantic locations
- `tests` - Organize pytest files, separate test-drivers  
- `scripts` - Categorize by purpose (demos, training, diagnostics, utilities)
- `config` - Consolidate configuration files
- `tasks` - Separate active tasks from archived work
- `root` - Clean up root directory scatter (high priority for file scatter)
- `repo` - Assistance in git operations

**Actions:**
1. **Analyze** current file placement vs semantic purpose
2. **Propose** new directory structure with rationale
3. **Execute** file moves with git history preservation
4. **Update** all pointer documents and cross-references
5. **Validate** no broken links or missing dependencies

### `repo-mode cache`

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
```markdown
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
```

## Organization Principles

### **Directory Structure Philosophy**
```
repo-root/
├── src/                    # Core application code
├── tests/                  # Automated pytest files only
├── scripts/
│   ├── demos/             # Demonstration scripts
│   ├── training/          # ML/AI training utilities
│   ├── diagnostics/       # Debug and analysis tools
│   └── test-drivers/      # Interactive test scripts
├── docs/
│   ├── guides/            # How-to documentation
│   ├── design/            # Architecture decisions
│   ├── analysis/          # Research and findings
│   └── status/            # Progress reports
├── tasks/                 # Active work management
├── config/                # Configuration files
└── data/                  # Test data and samples
```

### **File Naming Conventions**
- **Lowercase, hyphenated**: `feature-name.py`, `test-results.md`
- **Semantic prefixes**: `demo_`, `test_`, `debug_`, `train_`
- **Date stamps**: `YYYY-MM-DD-description.md` for temporal files
- **Version indicators**: `v2`, `enhanced`, `final` when necessary

### **Git Workflow Optimization**
- **Preserve history** during file moves using `git mv`
- **Atomic commits** for organizational changes
- **Clear commit messages** following conventional format
- **Branch protection** for structural changes

## Execution Protocol

### **Phase 1: Analysis**
1. **Scan repository** for file scatter and misplacement
2. **Identify semantic categories** and proper locations
3. **Map dependencies** and cross-references
4. **Assess impact** of proposed changes

### **Phase 2: Planning**
1. **Design optimal structure** with rationale
2. **Plan move sequence** to avoid breaking dependencies
3. **Identify pointer updates** required
4. **Prepare rollback strategy**

### **Phase 3: Execution**
1. **Execute file moves** with git history preservation
2. **Update documentation** pointers and references
3. **Validate functionality** after reorganization
4. **Create summary** of changes made

### **Phase 4: Validation**
1. **Test all workflows** still function
2. **Verify documentation** accuracy
3. **Confirm git history** preservation
4. **Update workspace** configuration if needed

## Success Criteria

### **Immediate Goals**
- [ ] Files in semantically appropriate locations
- [ ] No broken links or missing references
- [ ] Clean, navigable directory structure
- [ ] Preserved git history for moved files

### **Long-term Benefits**
- [ ] Improved developer onboarding experience
- [ ] Faster AI agent context loading
- [ ] Reduced cognitive overhead for navigation
- [ ] Maintainable documentation hierarchy

## Integration with Other Modes

- **task-mode**: Organize task files and update TASKS.md structure
- **doc-mode**: Clean up documentation after repo operations
- **review-mode**: Assess repository health post-organization
- **dev-session-mode**: Log organizational changes and decisions

## Quality Indicators

**Good Organization:**
- Semantic file placement matches purpose
- Clear directory hierarchy with logical grouping
- No orphaned or misplaced files
- Consistent naming conventions
- Updated cross-references
- **Root directory focused** on essential files only

**Poor Organization:**
- **Root directory file scatter** (>20 miscellaneous files)
- Mixed purposes in single directories
- Broken documentation links
- Inconsistent naming patterns
- Stale or outdated pointer documents

---

**Remember**: Repo-mode is about creating **sustainable, navigable structure** that serves both human developers and AI agents efficiently. Focus on **semantic organization** over alphabetical, and always **preserve functionality** during cleanup operations.

**Special Focus**: Root directory file scatter is a critical indicator of repository health - aim for <10 essential files in root directory for optimal navigation.
