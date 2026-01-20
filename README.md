# Personal Agent System

A modular, extensible personal AI agent designed to store ideas, track goals, reason about user input, and eventually act as a long-term planning and opportunity-generation assistant.

This project is built with a clean architecture that supports:
- Persistent JSON-based memory
- Idea and goal management (CRUD + completion)
- A command-driven agent interface
- Natural language fallback via an OpenAI-compatible LLM
- A scalable folder structure for future tools and capabilities

---

## Features

### Idea Management
- Add ideas
- List ideas
- Delete ideas

### Goal Management
- Add goals
- List goals
- Delete goals
- Mark goals as completed

### Memory System
- JSON-backed persistent storage
- Separate domains for ideas, goals, and profile data

### LLM Integration
- OpenAI-compatible client
- Natural language fallback when no command matches
- Modular design for swapping providers

### Agent Architecture
- Command routing for tools
- LLM reasoning for general queries
- Clean separation of concerns

---

## Project Structure
personal-agent/ CHANGELOG.md README.md src/ main.py agent/ agent.py tools/ idea_tools.py goal_tools.py memory/ memory.py llm/ llm_client.py data/ ideas.json progress.json profile.json .gitignor


---

## Installation

### 1. Clone the repository
git clone <your-repo-url> cd personal-agent


### 2. Install dependencies
pip install -r requirements.txt

(If you don’t have a requirements file yet, you can create one later.)

### 3. Set your API key

Set an environment variable:
export OPENAI_API_KEY="your-key-here"

On Windows PowerShell:
setx OPENAI_API_KEY "your-key-here"


---

## Running the Agent

From the project root:
python src/main.py

You’ll enter an interactive CLI where you can type commands like:
add idea: build a rental property analyzer list ideas add goal: increase monthly savings by 10% complete goal: 1 list goals

If no command matches, the agent uses the LLM to respond naturally.

---

## Roadmap (High-Level)

- Automatic tool selection via LLM reasoning
- Multi-step planning and task execution
- Reflection and self-improvement loops
- Vector memory for semantic recall
- Web search and external tool integrations
- Event scheduling and reminders
- Financial analysis and opportunity generation modules

---

## License

This project is currently private and unlicensed. Add a license file if you plan to share or open-source it.