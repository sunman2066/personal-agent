from tools.idea_tools import add_idea, list_ideas, delete_idea
from tools.goal_tools import add_goal, list_goals, delete_goal, complete_goal

class Agent:
    def __init__(self, llm_client, memory):
        self.llm = llm_client
        self.memory = memory

    def process(self, user_input):
        # Add idea
        if user_input.startswith("add idea:"):
            idea_text = user_input.replace("add idea:", "").strip()
            return add_idea(self.memory, idea_text)

        # List ideas
        if user_input == "list ideas":
            return list_ideas(self.memory)

        # Delete idea
        if user_input.startswith("delete idea:"):
            idea_id = user_input.replace("delete idea:", "").strip()
            return delete_idea(self.memory, idea_id)

        # Add goal
        if user_input.startswith("add goal:"):
            goal_text = user_input.replace("add goal:", "").strip()
            return add_goal(self.memory, goal_text)

        # List goals
        if user_input == "list goals":
            return list_goals(self.memory)

        # Delete goal
        if user_input.startswith("delete goal:"):
            goal_id = user_input.replace("delete goal:", "").strip()
            return delete_goal(self.memory, goal_id)

        # Complete goal
        if user_input.startswith("complete goal:"):
            goal_id = user_input.replace("complete goal:", "").strip()
            return complete_goal(self.memory, goal_id)

        # LLM fallback
        return self.llm.chat([
            {"role": "system", "content": "You are Bryan's personal agent. Be concise and helpful."},
            {"role": "user", "content": user_input}
        ])