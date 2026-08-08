from langchain_tavily import TavilyClient
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    return the list of the tools to be used
    """
    tools = [TavilyClient(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    create a tool node
    """
    return ToolNode(tools=tools)

