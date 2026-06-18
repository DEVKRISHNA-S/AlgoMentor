# app/main.py

import streamlit as st
from llm.ollama_client import ask_model


st.set_page_config(
    page_title="AlgoMentor",
    page_icon="🧠"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:

    st.title("AlgoMentor")

    mode = st.radio(
        "Choose Mode",
        [
            "chat",
            "problem Solver",
            "code Review"
        ]
    )

st.title("AlgoMentor")

st.write(
    "Learn DSA through guided hints, code reviews, and problem-solving."
)

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.text_area(
    "Your Question",
    height=150
)

if st.button("Ask Mentor"):

    if question:

        # Store user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.spinner("Thinking..."):

            answer = ask_model(
                st.session_state.messages,
                mode
            )

        # Store assistant message
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        # Display latest answer
        with st.chat_message("assistant"):
            st.markdown(answer)