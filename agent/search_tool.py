# agent/search_tool.py

from langchain_community.tools.tavily_search import TavilySearchResults

# Web search tool using Tavily API
tavily_search_tool = TavilySearchResults()
