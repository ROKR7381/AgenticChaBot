import streamlit as st
import os
from langchain_openai import AzureChatOpenAI

class AzureOpenAILLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            azure_openai_api_key = self.user_controls_input.get('AZURE_OPENAI_API_KEY', '')
            azure_openai_deployment_name = self.user_controls_input.get('AZURE_OPENAI_DEPLOYMENT_NAME', '')
            azure_openai_endpoint = self.user_controls_input.get('AZURE_OPENAI_ENDPOINT', '')
            azure_openai_api_version = self.user_controls_input.get('AZURE_OPENAI_API_VERSION', '')

            if azure_openai_api_key == "":
                st.error("Please Enter the Azure OpenAI API key")
                return None

            llm = AzureChatOpenAI(
                api_key = azure_openai_api_key,
                model = azure_openai_deployment_name,
                azure_endpoint = azure_openai_endpoint,
                api_version = azure_openai_api_version,
                
            )
        except Exception as e:
            raise ValueError(f"Error LLM not initiated {str(e)}")
        else:
            return llm