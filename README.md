# LangGraph MCP Chatbot

This project is a general-purpose conversational assistant built using LangGraph, with integrated web search powered by Tavily. The chatbot can understand natural language queries, retrieve up-to-date web content when necessary, and respond conversationally using OpenAI’s GPT models.

---

## Features

- Multi-turn conversation using LangGraph agents
- Automatic web search with Tavily for real-time information
- Clean, modular Python structure
- Command-line interface (CLI) interaction
- Optional web interface using Streamlit
- Easily configurable via `.env` file

---

## Tech Stack

- LangGraph for agent flow
- LangChain OpenAI for LLMs
- Tavily MCP for web search
- Streamlit (optional) for UI
- Python 3.9 or above

---

## Project Structure

```
langgraph-mcp-chatbot/
│
├── main.py                  # CLI runner for the chatbot
├── streamlit_ui.py          # Streamlit web interface (optional)
├── agent/                   # Agent logic
│   ├── __init__.py
│   ├── agent.py             # LangGraph executor setup
│   └── search_tool.py       # Tavily web search tool
│
├── .env                     # API keys (excluded from version control)
├── .gitignore               # Ignore venv, .env, pycache, etc.
├── requirements.txt         # Python dependencies
├── dev_log.md               # Development timeline and notes
└── README.md                # This file
```

---

## Setup

### 1. Clone and enter project

```bash
git clone https://github.com/your-username/langgraph-mcp-chatbot
cd langgraph-mcp-chatbot
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv
# Activate on Windows:
.venv\Scripts\activate
# Or on Unix/macOS:
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your `.env` file

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_key_here
TAVILY_API_KEY=your_tavily_key_here
```

---

## Running the Chatbot

### Option 1: CLI Interface

```bash
python main.py
```

Type your questions in the terminal. Type `exit` to quit.

### Option 2: Streamlit Interface (Optional)

```bash
streamlit run streamlit_ui.py
```

This launches a web-based chatbot interface in your browser.

---

## How It Works

- `main.py` starts a CLI input loop that collects user input.
- Input and previous messages are passed to a LangGraph agent.
- The agent decides whether to call a tool (Tavily) or respond directly.
- Output is printed or displayed.

---

## Example Queries

Try these to test functionality:

- What is the weather in Paris today?
- Who won the last Champions League final?
- What is LangGraph used for?

---

## Development Log

Refer to [dev_log.md](./dev_log.md) for a full build timeline and design choices.

---

## Status

- Core functionality complete
- Modular and documented code
- Tavily and LangGraph MCP integrated
- CLI interface functional
- Optional UI available with Streamlit

---

## License

MIT — free to use, modify, and distribute with credit.

---

## Acknowledgments

- LangGraph: https://github.com/langchain-ai/langgraph  
- Tavily API: https://docs.tavily.com