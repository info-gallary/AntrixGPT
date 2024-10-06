import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert assistant in space science, focusing on the solar system, space exploration, and how solar events affect Earth. Please provide accurate and detailed explanations."),
        ("user", "Question: {question}")
    ]
)

st.title("AntrixGPT 🚀")

input_text = st.text_input("Ask a question about space science or solar events:")

llm = Ollama(model="gemma:2b")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
