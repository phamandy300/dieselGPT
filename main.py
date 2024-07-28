import streamlit as st
from streamlit_chat import message

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)

def main():
    template = """
    Answer the question below.

    Here is the conversation history: {context}

    Question: {question}

    Answer: 
    """

    model = OllamaLLM(model="tinyllama")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    st.set_page_config(
        page_title="DieselGPT",
        page_icon="🎴"
    )


    st.header("Chat")

    with st.sidebar:
        user_input = st.text_input("Your message: ", key="user_input")
    
    message("Hello")

if __name__== "__main__":
    main()