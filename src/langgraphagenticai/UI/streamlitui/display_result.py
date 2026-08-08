import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json
import os

class DisplayResultStreamlit:
    def __init__(self, usecase,graph,user_message):
        self.usecase=usecase
        self.graph=graph
        self.user_message=user_message
        
    def stream_messages(self):
        for msg, _ in self.graph.stream(
            {'messages': ("user", self.user_message)},
            stream_mode="messages",
        ):
            if msg.content:
                yield msg.content

    def display_result_on_ui(self):
        usecase=self.usecase
        graph=self.graph
        user_message=self.user_message
        if usecase == "Basic Chatbot":
            with st.chat_message("user"):
                st.write(user_message)
            with st.chat_message('assistant'):
                st.write_stream(self.stream_messages())

                    
                        