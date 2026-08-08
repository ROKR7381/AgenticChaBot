import os
import streamlit as st
from langchain_openai import ChatOpenAI


class OpenAILLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            openai_api_key = self.user_controls_input['OPENAI_API_KEY']
            selected_openai_model = self.user_controls_input['selected_openai_model']
            openai_base_url = self.user_controls_input['OPENAI_BASE_URL']
            if openai_api_key=="" and os.environ['OPENAI_API_KEY'] == "":
                st.error("Please Enter the OpenAI API key")

            llm = ChatOpenAI(
                api_key = openai_api_key,
                model = selected_openai_model,
                base_url = openai_base_url,
                
            )
        except Exception as e:
            raise ValueError(f"Error LLM not initiated {str(e)}")
        else:
            return llm