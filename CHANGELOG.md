# Changelog

All notable changes to this project will be documented in this file.

This project follows semantic versioning and uses a simplified Keep a Changelog format.

---

## [1.0.0] - Initial Agent Stack

### Added
- Complete project structure under `src/` including:
  - `agent/`
  - `tools/`
  - `memory/`
  - `llm/`
  - `data/`
- Implemented persistent JSON-based memory system:
  - `profile.json`
  - `ideas.json`
  - `progress.json`
- Added Memory class with load/save functionality.
- Implemented Idea Tools:
  - `add_idea`
  - `list_ideas`
  - `delete_idea`
- Implemented Goal Tools:
  - `add_goal`
  - `list_goals`
  - `delete_goal`
  - `complete_goal`
- Added LLM client using OpenAI-compatible API.
- Created Agent class with:
  - Command routing for ideas and goals
  - LLM fallback for natural language responses
- Added main CLI loop in `main.py` for interactive use.

### Notes
- This version establishes the foundation for a modular, extensible personal agent.
- Future versions will introduce automatic tool selection, planning, and multi-step reasoning.

---

## [Unreleased]

### Planned
- Automatic tool invocation via LLM reasoning.
- Task planning and multi-step workflows.
- Reflection and self-improvement loops.
- Vector memory layer for semantic recall.
- Web search and external tool integrations.
