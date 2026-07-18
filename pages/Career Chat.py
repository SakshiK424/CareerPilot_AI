import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from models.llm import llm
from models.prompts import CAREER_SYSTEM_PROMPT

st.set_page_config(page_title="Career Chat", page_icon="💬")

st.title("💬 CareerPilot AI")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask your career question...")

if prompt:
    # Display user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Build message list
    messages = [
        SystemMessage(content=CAREER_SYSTEM_PROMPT)
    ]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(messages)

        st.markdown(response.content)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.content
        }
    )