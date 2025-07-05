# main.py

import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from agent.agent import create_agent_graph  # updated import

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

# Sanity check for required keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY or not OPENAI_API_KEY.startswith("sk-"):
    raise ValueError("Missing or invalid OPENAI_API_KEY in .env file.")

# Initialize agent
graph = create_agent_graph()

# Launch CLI chatbot
print("LangGraph Chatbot is running (type 'exit' to quit)")
state = {"messages": []}

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        print("Exiting chatbot.")
        break

    # Add user input to conversation state
    state["messages"].append(HumanMessage(content=user_input))

    # Get agent response
    result = graph.invoke(state)

    # Print response
    reply = result["messages"][-1].content
    print(f"Bot: {reply}")

    # Update state
    state = result
