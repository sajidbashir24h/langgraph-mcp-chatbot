# Development Log - LangGraph MCP Chatbot

This log outlines the development process for the LangGraph MCP Chatbot, including planning, implementation, and testing phases.

---

## Day 1: Initial Planning and Setup

- Read and reviewed the challenge requirements.
- Identified core components: LangGraph, Tavily, OpenAI API.
- Decided to begin with a CLI-based chatbot for simplicity.
- Initialized project folder and Python virtual environment.
- Created `.gitignore` and `.env` files.
- Installed required libraries as per project stack.

## Day 2: First Functional Prototype

- Implemented `main.py` with basic CLI loop.
- Created `agent.py` to set up LangGraph executor and OpenAI LLM.
- Integrated `TavilySearchResults` as a search tool in `search_tool.py`.
- Validated API key loading and added error handling.
- Tested chatbot's basic ability to converse and invoke web search.

## Day 3: Refactor and Modularization

- Structured code into a proper Python package under `agent/`.
- Added `__init__.py` for package recognition.
- Separated agent creation and search logic into modular files.
- Verified that CLI chatbot worked with updated import paths.
- Cleaned and added explanatory comments to complex logic.

## Day 4: Documentation and Streamlit UI

- Created a clear and professional `README.md` with setup and run instructions.
- Drafted this development log.
- Developed optional `streamlit_ui.py` file for a simple browser interface.
- Confirmed Streamlit version works locally using the same agent logic.
- Added `.env` and `.gitignore` compliance checks for security and hygiene.

---

## Status Summary

- Core chatbot functionality completed and tested
- CLI chatbot fully working with LangGraph and Tavily integration
- Development log and documentation finalized
- Streamlit UI completed as optional feature

---

## Next Steps (Optional)

- Enhance agent with memory handling or context re-ranking
- Improve search result formatting
- Add unit tests and deployment script for production

---

## Tools Used

- LangGraph MCP
- LangChain OpenAI (chat model)
- Tavily MCP web search
- Python 3.9
- Streamlit (for demo UI)
- dotenv for managing API credentials