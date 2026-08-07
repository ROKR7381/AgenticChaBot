import streamlit as st
import os

from src.langgraphagenticai.UI.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())


        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            selected_llm = st.selectbox("Select LLM", llm_options)
            self.user_controls["selected_llm"] = selected_llm

            if selected_llm == 'GROQ':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.text_input("API Key",type="password")
                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")

            elif selected_llm == 'AZUREOPENAI':
                # Model selection
                model_options = self.config.get_azure_openai_model_options()
                self.user_controls["selected_azure_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["AZURE_OPENAI_API_KEY"] = st.session_state["AZURE_OPENAI_API_KEY"]=st.text_input("API Key",type="password")
                self.user_controls["AZURE_OPENAI_ENDPOINT"] = st.session_state["AZURE_OPENAI_ENDPOINT"]=st.text_input("Endpoint")
                self.user_controls["AZURE_OPENAI_API_VERSION"] = st.session_state["AZURE_OPENAI_API_VERSION"]=st.text_input("API Version", value="2024-06-01")
                self.user_controls["AZURE_OPENAI_DEPLOYMENT_NAME"] = st.session_state["AZURE_OPENAI_DEPLOYMENT_NAME"]=st.text_input("Deployment Name")
                # Validate API key
                if not self.user_controls["AZURE_OPENAI_API_KEY"]:
                    st.warning("⚠️ Please enter your Azure OpenAI API key to proceed. Don't have? refer : https://azure.microsoft.com/en-us/products/ai-services/openai-service ")

            elif selected_llm == 'OPENAI':
                # Model selection
                model_options = self.config.get_openai_model_options()
                self.user_controls["selected_openai_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["OPENAI_API_KEY"] = st.session_state["OPENAI_API_KEY"]=st.text_input("API Key",type="password")
                self.user_controls["OPENAI_BASE_URL"] = st.session_state["OPENAI_BASE_URL"]=st.text_input("Base URL (optional)", placeholder="https://api.openai.com/v1")
                # Validate API key
                if not self.user_controls["OPENAI_API_KEY"]:
                    st.warning("⚠️ Please enter your OpenAI API key to proceed. Don't have? refer : https://platform.openai.com/api-keys ")
            
            ## USecase selection
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecases",usecase_options)

        return self.user_controls

    
