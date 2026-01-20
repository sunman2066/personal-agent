# Contributing Guide

Thank you for your interest in contributing to the Personal Agent System.  
This document outlines the standards, workflows, and expectations for contributing to the project.

Even if you are the sole contributor today, this guide ensures consistency and clarity as the project grows.

---

## Development Philosophy

This project is built with the following principles:

- **Modularity** — Each component should do one thing well.
- **Extensibility** — New tools and capabilities should be easy to add.
- **Transparency** — Code should be readable, predictable, and well-structured.
- **Safety** — The agent should behave responsibly and avoid unintended actions.
- **Local-first** — The system should run locally without requiring cloud infrastructure.

---

## Project Structure

All source code lives under `src/`:
src/ main.py agent/ tools/ memory/ llm/

Persistent data lives under `data/`.

Documentation lives at the project root.

---

## Branching Strategy

Use a simple, clear workflow:

- `main` — stable, working code
- `feature/<name>` — new features or improvements
- `fix/<name>` — bug fixes

Example:
git checkout -b feature/tool-selection

---

## Commit Guidelines

Write clear, descriptive commit messages:

- Use the imperative mood: “Add goal completion tool”
- Keep the first line under 72 characters
- Include context when needed

Examples:
Add automatic goal completion tool Refactor memory layer for clarity Fix import path issue in agent router

---

## Code Style

- Follow Python best practices (PEP 8 where reasonable)
- Keep functions small and focused
- Prefer pure functions for tools
- Avoid deeply nested logic
- Use descriptive variable names
- Keep imports organized and minimal

---

## Adding New Tools

When adding a new tool:

1. Create a file in `src/tools/`
2. Implement the tool as a pure function
3. Update the agent router (or tool-selection logic in future versions)
4. Add tests or manual usage examples
5. Update the README if needed

---

## Updating Documentation

Whenever you add or change functionality:

- Update `CHANGELOG.md`
- Update `README.md` if usage changes
- Update `ROADMAP.md` if direction changes

Documentation is part of the codebase.

---

## Testing

At this stage, manual testing through the CLI is acceptable:
python src/main.py

As the project grows, a `tests/` directory will be added for automated testing.

---

## Pull Requests (Future)

If this project becomes collaborative:

- Keep PRs small and focused
- Reference issues or roadmap items
- Include before/after behavior when relevant

---

## Questions or Ideas

If you have new ideas, improvements, or architectural changes in mind, document them in:

- `ROADMAP.md` for future plans
- `CHANGELOG.md` for completed changes
- `README.md` for usage changes

This keeps the project coherent and evolving intentionally.