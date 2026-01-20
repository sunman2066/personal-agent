from datetime import datetime

def add_goal(memory, goal_text):
    goals = memory.load("progress")

    goal_id = str(len(goals) + 1)

    goals[goal_id] = {
        "text": goal_text,
        "created_at": datetime.utcnow().isoformat(),
        "completed": False
    }

    memory.save("progress", goals)

    return f"Goal saved with ID {goal_id}"


def list_goals(memory):
    goals = memory.load("progress")

    if not goals:
        return "No goals saved yet."

    lines = []
    for goal_id, data in goals.items():
        status = "✓" if data.get("completed") else "•"
        lines.append(f"{goal_id}: {status} {data['text']}")

    return "\n".join(lines)


def delete_goal(memory, goal_id):
    goals = memory.load("progress")

    if goal_id not in goals:
        return f"No goal found with ID {goal_id}"

    deleted = goals.pop(goal_id)
    memory.save("progress", goals)

    return f"Deleted goal {goal_id}: {deleted['text']}"

def complete_goal(memory, goal_id):
    goals = memory.load("progress")

    if goal_id not in goals:
        return f"No goal found with ID {goal_id}"

    goals[goal_id]["completed"] = True
    memory.save("progress", goals)

    return f"Marked goal {goal_id} as completed."

