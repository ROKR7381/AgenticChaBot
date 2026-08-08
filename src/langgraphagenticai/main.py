import streamlit as st

from src.langgraphagenticai.UI.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.LLMS.openaillm import OpenAILLM
from src.langgraphagenticai.LLMS.azureopenaillm import AzureOpenAILLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.UI.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    Load and runs the LangGraph Agentic AI application with streamlit UI.
    This function initializes the UI , handles user input, config the LLM Models,
    Sets up the graph based on the selected use case, and display the output while
    implementing exception handling for robustness.
    """

    ## Load ui
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui() 

    if not user_input:
        st.error("ERROR: Failed to load user input from the UI")
        return

    user_message = st.chat_input("Enter your messages")

    if user_message:
        try:
            selected_llm = user_input.get("selected_llm")
            if selected_llm == "GROQ":
                obj_llm_config = GroqLLM(user_controls_input=user_input)
            elif selected_llm == "OPENAI":
                obj_llm_config = OpenAILLM(user_controls_input=user_input)
            elif selected_llm == "AZUREOPENAI":
                obj_llm_config = AzureOpenAILLM(user_controls_input=user_input)
            else:
                st.error("Error: Invalid LLM selected.")
                return

            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initiated, please check the API key and model name")
                return
            usecase = user_input.get('selected_usecase')

            if not usecase:
                st.error("Error: Invalid usecase selected.")
                return
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Error setting up graph: {str(e)}")
                return

        except Exception as e:
            st.error(f"Error initializing app: {str(e)}")
