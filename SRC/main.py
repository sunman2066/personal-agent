from agent.agent import Agent
from memory.memory import Memory
from llm.llm_client import LLMClient

def main():
    # Initialize memory and LLM
    memory = Memory()
    llm = LLMClient()  # Uses OPENAI_API_KEY from environment

    # Create the agent
    agent = Agent(llm_client=llm, memory=memory)

    # CLI loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye.")
            break

        response = agent.process(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    main()