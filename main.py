import streamlit as st
from streamlit_chat import message

from langchain_ollama import ChatOllama
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)

def main():
    model = ChatOllama(model="llama3")
 
    if "context" not in st.session_state:
        st.session_state.context = [
            SystemMessage(content="You are a helpful assistant.")
        ]

    st.set_page_config(
        page_title="dieselGPT",
        page_icon="🎴"
    )

    st.header("Chat")

    with st.sidebar:
        user_input = st.text_input("Your message: ", key="user_input")
    
        if user_input:
            st.session_state.context.append(HumanMessage(content=user_input))
            with st.spinner():
                response = model.invoke(st.session_state.context)
            st.session_state.context.append(AIMessage(content=response.content))

    context = st.session_state.get('context', [])
    for i, msg in enumerate(context[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')

if __name__== "__main__":
    main()