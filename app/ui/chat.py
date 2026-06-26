# app/ui/chat.py

import streamlit as st

from llm.ollama_client import ask_model


def render_chat():

    st.header("Chat")

    # Display previous conversation
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if (
                message["role"] == "assistant"
                and "sources" in message
                and message["sources"]
            ):

                with st.expander("📚 Sources Used"):

                    for doc in message["sources"]:

                        st.markdown(f"**📄 {doc['source']}**")
                        st.caption(doc["content"][:150] + "...")
                        st.divider()

    question = st.text_area(
        "Ask a DSA Question",
        height=250
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

                result = ask_model(
                    st.session_state.messages,
                    "Chat"
                )

            # Store assistant message
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": result["sources"]
                }
            )

            st.rerun()