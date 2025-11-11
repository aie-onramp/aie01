# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

AIEO1 is an educational bootcamp repository for the AI Engineer Onramp course. This is a 4-week intensive program teaching professional AI engineering practices, focusing on transitioning from experimental coding to structured, production-ready LLM application development.

**Course Structure:**
- Session 1: LLM APIs & AI-Assisted Development (Python/Jupyter)
- Session 2: Front End UI Development & Deployment (Next.js/Vercel)
- Session 3: Back End Web App Development & Deployment (FastAPI/Render)
- Session 4: End-to-End LLM Application Development with Coding Agents

## Development Commands

### Session 1 (Python/Jupyter)
```bash
# Install Python dependencies
uv sync

# Launch Jupyter notebook environment
jupyter notebook
```

### Session 2 (Frontend/Next.js)
```bash
# Install Node.js dependencies
npm install

# Run development server (localhost:3000)
npm run dev

# Install Vercel CLI for deployment
npm install -g vercel
```

### Git Workflow Commands

This repository uses a dual-remote pattern where students maintain their own repo (origin) while pulling course materials from upstream (AI-Maker-Space/AIEO1).

```bash
# Create and work on feature branches
git switch -c feature/feature-name

# Merge features with preserved history
git merge --no-ff feature/feature-name

# Clean up branches after merging
git branch -d feature/feature-name
git push origin --delete feature/feature-name

# Sync from upstream course repository
git fetch upstream
git merge upstream/main
```

## High-Level Architecture

### Pedagogical Pattern: Progressive Complexity

The course is structured to build skills incrementally:

1. **Session 1:** API fundamentals using Jupyter notebooks and OpenAI SDK
2. **Session 2:** Frontend scaffolding with v0.dev, deployment to Vercel
3. **Session 3:** Backend integration with FastAPI (upcoming)
4. **Session 4:** Full-stack applications with coding agents (upcoming)

### Git Flow Strategy

```
main (production-ready code)
└── develop
    ├── feature/feature-1
    ├── feature/feature-2
    └── feature/feature-3
```

**Key Principles:**
- Never work directly on `main` branch
- All changes developed in feature branches
- Use `--no-ff` merges to preserve feature branch history
- Simulates multi-agent parallel development workflow

### AI-Assisted Development Stack

- **Cursor IDE:** Primary development environment with custom code generation rules
- **v0.dev:** AI-powered frontend scaffolding tool (Vercel)
- **OpenAI API:** Core LLM integration for applications
- **CI/CD:** Automatic GitHub → Vercel deployments

### Dual-Remote Repository Pattern

Students maintain two remotes:
- **origin:** Personal repository for assignments and experiments
- **upstream:** Course repository (AI-Maker-Space/AIEO1) for pulling updates

This allows following course material while maintaining independent work.

## Code Style Conventions

From [Session_02_Front_End_UI_Development_&_Deployment_of_LLM_Applications/cursor_rules.md](Session_02_Front_End_UI_Development_&_Deployment_of_LLM_Applications/cursor_rules.md):

### Naming Conventions
- **camelCase:** Variables and functions
- **PascalCase:** React components and classes
- **UPPER_SNAKE_CASE:** Constants and environment variables

### Code Organization
- One main entry point per application
- Descriptive folder names for components
- File size warning threshold: 300 lines
- Prefer absolute import paths over relative paths

### Project Structure
- Keep components modular and focused
- Separate business logic from UI components
- Maintain consistent file organization within session directories

## Important Context

### Repository Structure Notes

- **No root package.json:** This is an educational repository, not a single application. Each session has its own dependencies.
- **Session-specific configurations:**
  - Session 1 uses `pyproject.toml` for Python dependencies
  - Session 2 projects have their own Next.js configurations
- **Separate entry points:** Each session has distinct learning objectives and technical stacks

### Working with This Repository

1. **This is a learning repository:** Code quality standards are educational, not production
2. **Feature branch workflow is pedagogical:** Teaches professional Git practices and simulates team development
3. **All assignments deploy to production:** Students create shareable, deployed applications
4. **Session 2 workflow:** v0.dev generates initial code → students customize → deploy to Vercel

### Key Files and Locations

- **Session 1 notebook:** [Session_01_LLM_APIs_&_AI-Assisted_Development/OpenAI_playground_for_developers.ipynb](Session_01_LLM_APIs_&_AI-Assisted_Development/OpenAI_playground_for_developers.ipynb)
- **Session 2 assignment:** [Session_02_Front_End_UI_Development_&_Deployment_of_LLM_Applications/Assignment.md](Session_02_Front_End_UI_Development_&_Deployment_of_LLM_Applications/Assignment.md)
- **Git setup instructions:** [00_Setting_Up_GitHub/README.md](00_Setting_Up_GitHub/README.md)
- **Course resources:** [README.md](README.md)

### Dependencies Management

**Python (Session 1):**
- Package manager: `uv` (Astral's modern pip replacement)
- Python version: >=3.8
- Key packages: openai, jupyter, python-dotenv

**Node.js (Session 2):**
- Framework: Next.js
- UI libraries: shadcn/ui, Tailwind CSS
- Deployment: Vercel CLI

### Environment Configuration

- **Claude Code permissions:** [.claude/settings.local.json](.claude/settings.local.json) allows `git remote set-url` commands
- **Environment variables:** Use `.env` files (gitignored) for API keys
- **IDE settings:** Cursor-specific configurations in session directories

## Session-Specific Guidance

### Session 1: LLM APIs & AI-Assisted Development
- Work within Jupyter notebooks for experimentation
- Focus on OpenAI API patterns: zero-shot, few-shot, chain-of-thought
- Implement "LLM as judge" evaluation frameworks
- Helper functions defined in notebook for prompt formatting

### Session 2: Front End UI Development & Deployment
- Use v0.dev to generate initial Next.js scaffolding
- Follow breakout room tutorial for deployment workflow
- Create multiple feature branches to simulate multi-agent development
- Deploy to Vercel with automatic CI/CD
- Reference [BreakoutRoom.md](Session_02_Front_End_UI_Development_&_Deployment_of_LLM_Applications/BreakoutRoom.md) for step-by-step guidance
