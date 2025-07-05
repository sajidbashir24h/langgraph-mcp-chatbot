# streamlit_ui.py

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from agent.agent import create_agent_graph

# Load environment variables from .env
load_dotenv()

# Ensure API keys are present
if not os.getenv("OPENAI_API_KEY"):
    st.error("Missing OpenAI API key. Check your .env file.")
    st.stop()

# Initialize agent
graph = create_agent_graph()

# Streamlit UI setup
st.set_page_config(page_title="LangGraph Chatbot", page_icon="🤖")
st.title("🧠 LangGraph MCP Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat input
user_input = st.chat_input("Ask me anything...")
if user_input:
    # Append user input
    st.session_state["messages"].append(HumanMessage(content=user_input))

    # Process through LangGraph agent
    with st.spinner("Thinking..."):
        result = graph.invoke({"messages": st.session_state["messages"]})
        bot_reply = result["messages"][-1].content
        st.session_state["messages"] = result["messages"]

# Display messages
for msg in st.session_state["messages"]:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").markdown(msg.content)
    else:
        st.chat_message("assistant").markdown(msg.content)
