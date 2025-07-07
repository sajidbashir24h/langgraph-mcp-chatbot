# agent/agent.py

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import chat_agent_executor
from agent.search_tool import tavily_search_tool  

def create_agent_graph():
    """
    Initializes the LangChain OpenAI chat model and sets up
    the LangGraph agent executor with the specified tools (Take messages,Think,Decide,Respond). 
    """

    llm = ChatOpenAI(model="gpt-3.5-turbo")  # Chat model initialization
    tools = [tavily_search_tool]            # Add web search as tool

    # Create the LangGraph agent executor with the chat model and tools 
    return chat_agent_executor.create_tool_calling_executor(
        model=llm,
        tools=tools
    )
