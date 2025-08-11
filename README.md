# VSCode Vibe-Centric Project Template

## Quick Start

1. **Copy this template to new project directory**
2. **Rename template files**: Remove `-TEMPLATE` suffix from core files
3. **Customize PROJECT.md**: Update for your specific project goals
4. **Initialize tasks**: Create `tasks/tasks.md` and your first task `tasks/task-0-repo-setup.md`
5. **Scaffold a project** (optional):
	- Python: scripts/utilities/scaffold-project.py --type python --name myproj --out ../myproj
	- Terraform: scripts/utilities/scaffold-project.py --type terraform --name myinfra --out ../myinfra
6. **Start first session**: Use `devsession` snippet in VS Code

## Workflow

- Start each session by checking `tasks/tasks.md` for quick wins.
- Use modular `tasks/task-N-$shortname.md` files for focused work.
- Track sessions notes in `sessions/dev-sessions.md`.
- Apply 80/20 model split between premium and coding models (eg Claude for analysis, GPT for coding).

## Output Standards

- All intermediate outputs should be in Markdown format, human-readable, and suitable for LLM input.
- Final outputs should be structured for the intended use case (e.g., STIX, Storm language).

## Key Features

- 🚀 **Flow-optimized structure** for rapid iteration
- 🤖 **AI-assisted development** with clear model roles  
- 📊 **Session tracking** for continuous improvement
- 🎯 **Bite-sized tasks** that maintain momentum

See `docs/VIBE-CENTRIC-FLOW.llm.md` for detailed workflow guide.
