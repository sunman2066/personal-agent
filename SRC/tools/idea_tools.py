from datetime import datetime

def add_idea(memory, idea_text):
    ideas = memory.load("ideas")

    idea_id = str(len(ideas) + 1)

    ideas[idea_id] = {
        "text": idea_text,
        "created_at": datetime.utcnow().isoformat()
    }

    memory.save("ideas", ideas)

    return f"Idea saved with ID {idea_id}"

def list_ideas(memory):
    ideas = memory.load("ideas")

    if not ideas:
        return "No ideas saved yet."

    lines = []
    for idea_id, data in ideas.items():
        lines.append(f"{idea_id}: {data['text']}")

    return "\n".join(lines)

def delete_idea(memory, idea_id):
    ideas = memory.load("ideas")

    if idea_id not in ideas:
        return f"No idea found with ID {idea_id}"

    deleted = ideas.pop(idea_id)
    memory.save("ideas", ideas)

    return f"Deleted idea {idea_id}: {deleted['text']}"