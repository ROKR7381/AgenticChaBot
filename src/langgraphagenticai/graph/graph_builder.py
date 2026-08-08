from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition, ToolNode


class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Build a Basic chatbot using Langgraph.

        """
        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        self.graph_builder.add_node('chatbot',self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_edge('chatbot',END)

        def chatbot_tools_build_graph(self):
            """
            Build a advance chatbot graph with tool integration.
            This Method creates a chatbot graph that includes a both chatbot node
            and a tool node. It defines tools , initializes the chatbot with tools
            capabilities, and set up conditional and direct edges between nodes.
            The chatbot node is the set as the entry point. If the chatbot node determines
            that tools are required , it will route to the tool node, otherwise it
            will directly produce the final response. Finally the graph ends at the end node.

            """
            ## Define the toola and tool node
            tools = get_tools()
            tool_node = create_tool_node(tools)

            ## define the LLM
            llm = self.llm

            ## define the chatbot node


            ## add nodes

            self.graph_builder.add_node("chatbot","")
            self.graph_builder.add_node('tools',tool_node)

            self.graph_builder.add_edge(START,'chatbot')
            self.graph_builder.add_conditional_edges("chatbot",tools_condition)
            self.graph_builder.add_edge('tools','chatbot')
            self.graph_builder.add_edge('chatbot',END)

            
    


    def setup_graph(self, usecase:str):
        """
        Sets up the graph for the selected use case
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot with Web":
            self.chatbot_tools_build_graph()
        return self.graph_builder.compile()
        
