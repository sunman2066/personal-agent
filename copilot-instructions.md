# Copilot Instructions for Personal Agent System

## Project Overview
A modular personal AI agent for managing ideas, tracking goals, and reasoning about user input via LLM integration. Architecture separates concerns: **Agent** routes commands, **Memory** persists JSON data, **Tools** implement CRUD operations, **LLMClient** provides natural language fallback.

---

## Architecture & Data Flow

### Core Components
- **Agent** (`SRC/agent/agent.py`): Command dispatcher with string pattern matching → tool routing or LLM fallback
- **Memory** (`SRC/memory/memory.py`): JSON-based persistence (3 domains: `profile.json`, `ideas.json`, `progress.json`)
- **Tools** (`SRC/tools/`): Stateless functions accepting `memory` object, returning formatted strings
- **LLMClient** (`SRC/LLM/llm_client.py`): OpenAI-compatible wrapper using `OPENAI_API_KEY` env var

### Data Flow
1. User input → `agent.process()` 
2. Pattern match checks in sequence (exact match for "list", prefix match for "add"/"delete")
3. Tool executes (reads memory, modifies, saves, returns string) OR LLM chain (system prompt + user input)
4. String response returned to CLI

### Key Design Patterns
- **Memory as parameter**: All tools receive `memory` object and call `memory.load(key)` / `memory.save(key, data)`
- **ID generation**: String IDs as dict keys (`str(len(dict) + 1)`); not UUID-based—**fragile**, fix during scaling
- **Timestamp storage**: ISO format UTC (`datetime.utcnow().isoformat()`)
- **Return strings**: Tools always return formatted strings, never structured data (matches LLM response type)

---

## Developer Workflows

### Running the Agent
```bash
python src/main.py
```
CLI prompts for commands. Type commands like:
- `add idea: build rental property analyzer`
- `list goals`
- `complete goal: 1`
- `anything else` → LLM fallback

### Adding New Tools
1. Create function in `SRC/tools/{domain}_tools.py` accepting `memory` parameter
2. Import in `SRC/agent/agent.py`
3. Add pattern match in `agent.process()` method
4. Return formatted string result

Example (new tool):
```python
# In tools/opportunity_tools.py
def score_idea(memory, idea_id):
    ideas = memory.load("ideas")
    if idea_id not in ideas:
        return f"Idea {idea_id} not found"
    # scoring logic
    return f"Score: 8/10 — Moderate potential"

# In agent.py
from tools.opportunity_tools import score_idea
# Then in process():
if user_input.startswith("score idea:"):
    idea_id = user_input.replace("score idea:", "").strip()
    return score_idea(self.memory, idea_id)
```

### Environment Setup
- Requires `OPENAI_API_KEY` env var (PowerShell: `setx OPENAI_API_KEY "key-here"`)
- `requirements.txt` is empty—add dependencies as needed (requests already used)
- Python 3.8+

---

## Project Conventions & Pitfalls

### ID Management (⚠️ Known Issue & Migration Plan)
IDs are auto-incremented strings based on dict length—**breaks on delete** (IDs reuse/conflict). 

**Migration Timeline:**
- **Now**: Document pattern; acceptable for single-user prototype
- **Before adding financial tools**: Migrate to UUIDs (Phase 1 priority per roadmap)
- **Migration steps**: 
  1. Update `id_generation` logic in tools to use `uuid.uuid4().hex`
  2. Add migration script to convert existing `data/*.json` files
  3. Update Agent's pattern matching to handle both old/new ID formats during transition
  4. Run on local data; commit migrated state

Current impact: low (small personal data sets); fix before multi-user access.

### Memory Structure
- `ideas.json`: `{id: {text, created_at}, ...}`
- `progress.json`: `{id: {text, created_at, completed: bool}, ...}` (goals stored here, not separate file)
- `profile.json`: Currently unused; reserved for user preferences/metadata

### Command Routing Order
Pattern matches execute in **sequence**—no priority system. Order in `agent.process()` determines precedence. Exact matches ("list ideas") process before prefix matches ("add idea:").

### LLM Integration
- Model: `gpt-4o-mini` (hardcoded; configurable via `chat()` parameter)
- System prompt in agent: "You are Bryan's personal agent. Be concise and helpful." (update if role changes)
- No function calling or structured output—only message content extracted

**Suggested Tone Profiles** (update system prompt as agent evolves):
- **Strategic & Analytical**: For financial analysis, opportunity evaluation ("Analyze this idea's financial viability considering..."). Emphasize reasoning, trade-offs, risk factors.
- **Encouraging but Honest**: For goal feedback, idea vetting ("This has potential. Here's what needs work..."). Balance optimism with constructive critique.
- **Transparent**: Explain reasoning chains, assumptions, decision factors. Avoid black-box answers.
- **Action-Oriented**: Move from analysis to next steps ("You should...", "Try..."). Drive execution.
- **Risk-Aware**: Flag legal/ethical concerns proactively ("This strategy is risky because..."). Align with personal values (long-term stability for kids).

---

## Cross-Component Communication

### Memory Access Pattern
```python
# Load
data = memory.load("ideas")  # Returns dict

# Modify
data["new_id"] = {...}

# Save
memory.save("ideas", data)  # Writes to JSON, auto-formats
```

### Tool-to-Agent Integration
Tools never instantiate memory/LLM—passed as dependencies. Enables testing and prevents circular imports.

### LLM Output Handling
`llm.chat(messages)` returns string directly (extracts `response.json()["choices"][0]["message"]["content"]`). Errors raise `HTTPError` if request fails.

---

## Future Architecture Notes (From Roadmap)

### Phase 1 Priority
Automatic tool selection via LLM reasoning (currently manual dispatch in agent.process())
- Agent should pass tool schema to LLM and let it decide which tool to call
- Requires structured output or JSON parsing from LLM
- Unblocks intelligent multi-step workflows

### Planned Tool Categories

**1. Financial Analysis** (highest priority)
- `analyze_opportunity()` – Evaluate business ideas for ROI, risks, capital requirements
- `estimate_returns()` – Project financial outcomes (rental property, investments, etc.)
- `budget_tracker()` – Monitor spending vs. goals
- `compare_strategies()` – Side-by-side analysis of wealth-building approaches

**2. Opportunity Generation**
- `generate_ideas()` – Brainstorm opportunities in specific domains (real estate, side income, etc.)
- `market_scan()` – Monitor trends, emerging opportunities (via web search integration)
- `validate_market_fit()` – Assess demand for a proposed idea

**3. Goal Planning & Execution** (exists: add enhancements)
- `create_milestone_plan()` – Break goals into measurable steps with timelines
- `set_reminders()` – Trigger notifications for goal check-ins
- `track_progress()` – Update and visualize progress toward goals

**4. Decision Support**
- `risk_assessment()` – Flag legal/ethical red flags
- `tradeoff_analysis()` – Compare options systematically
- `scenario_planning()` – Model outcomes under different conditions

**5. Integration Points** (future)
- Web search API – Market research, pricing data
- AWS services – Cloud cost analysis (if you scale to AWS-based tools)
- Calendar/scheduler – Event coordination
- External financial APIs – Real market data

### Memory Expansion
Vector embeddings for semantic recall (beyond current JSON key-value). Enables queries like "ideas similar to real estate" or "past decisions about passive income."

---

## Quick Reference

| File | Purpose | Key Function |
|------|---------|--------------|
| `SRC/main.py` | Entry point | Initializes Memory, LLMClient, Agent; CLI loop |
| `SRC/agent/agent.py` | Command dispatcher | `process(user_input)` routes to tools or LLM |
| `SRC/memory/memory.py` | Data persistence | `load(key)`, `save(key, data)` |
| `SRC/tools/idea_tools.py` | Idea CRUD | `add_idea()`, `list_ideas()`, `delete_idea()` |
| `SRC/tools/goal_tools.py` | Goal CRUD | `add_goal()`, `list_goals()`, `delete_goal()`, `complete_goal()` |
| `SRC/LLM/llm_client.py` | LLM wrapper | `chat(messages, model)` |

---

## Testing & Debugging

### Unit Testing Tools
Test tool functions in isolation by mocking memory:
```python
# tests/test_idea_tools.py
from tools.idea_tools import add_idea
from unittest.mock import Mock

def test_add_idea():
    mock_memory = Mock()
    mock_memory.load.return_value = {}
    
    result = add_idea(mock_memory, "test idea")
    
    assert "Idea saved with ID 1" in result
    mock_memory.save.assert_called_once()
```

### Memory Persistence Testing
Verify JSON I/O doesn't corrupt data:
```bash
# After running agent commands, inspect data files
cat data/ideas.json
cat data/progress.json
```
Ensure: valid JSON format, IDs are consistent, timestamps are ISO format, no data loss after save/load cycles.

### Command Routing Verification
Test agent.process() against all command patterns:
```python
# Verify exact matches execute first
assert "list ideas" matches before "list" prefix
# Verify prefix extraction works
user_input = "add idea: test"
assert extract_text(user_input) == "test"
```

### LLM Integration Testing
- Mock `LLMClient.chat()` during development (use mock responses)
- Test with real API key in staging/isolated environment only
- Verify system prompt is included in every request
- Log request/response pairs for debugging (redact API key)

### Debugging Tips
1. **Memory state inspection**: Print `memory.load(key)` at tool entry to verify incoming state
2. **Pattern match order**: Add debug print in `agent.process()` to see which pattern matched first
3. **ID conflicts**: Check `progress.json` and `ideas.json` for duplicate IDs after deletes
4. **LLM failures**: Catch `HTTPError` and log full response (status code, error message)
5. **Timestamp debugging**: Verify all timestamps are UTC ISO format (`2026-01-20T...Z`)
