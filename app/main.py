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
            "Chat",
            "Problem Solver",
            "Code Review"
        ]
    )

    st.divider()

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()


# Dynamic UI based on mode
if mode == "Problem Solver":
    input_label = "Paste LeetCode / Codeforces Problem"
    button_text = "Analyze Problem"

elif mode == "Code Review":
    input_label = "Paste Your Code"
    button_text = "Review Code"

else:
    input_label = "Ask a DSA Question"
    button_text = "Ask Mentor"


st.title("AlgoMentor")

st.header(mode)

st.write(
    "Learn DSA through guided hints, code reviews, and problem-solving."
)


# Display conversation history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.text_area(
    input_label,
    height=250
)


if st.button(button_text):

    if question:

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

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()