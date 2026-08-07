from ast import Load
import streamlit as st
from src.langgraphagenticai.UI.streamlitui.loadui import LoadStreamlitUI


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

    # if user_message:
    #     try:
    #         obj_llm_config = GroqLLM(user_controls_input=user_input)
    #         model = obj_llm_config.get_llm_model()

    #         if not model:
    #             st.error("Error: LLM model could not be initiated, please check the API key and model name")
    #             return


                

    
        