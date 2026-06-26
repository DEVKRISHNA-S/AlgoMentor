from pathlib import Path

from ollama import chat

from rag.retriever import retrieve


PROMPT_PATH = Path("app/prompts/mentor.txt")


def load_prompt(mode: str):

    if mode == "Chat":
        prompt_path = Path("app/prompts/mentor.txt")

    elif mode == "Problem Solver":
        prompt_path = Path("app/prompts/problem_solver.txt")

    elif mode == "Code Review":
        prompt_path = Path("app/prompts/code_review.txt")

    else:
        prompt_path = Path("app/prompts/mentor.txt")

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()


def clean_response(text: str):

    if "</think>" in text:
        text = text.split("</think>")[-1]

    return text.strip()


def ask_model(messages, mode):

    prompt = load_prompt(mode)

    latest_question = ""

    for msg in reversed(messages):

        if msg["role"] == "user":

            latest_question = msg["content"]
            break

    try:

        retrieved_docs = retrieve(
            latest_question,
            k=3
        )

        context_parts = []

        for doc in retrieved_docs:

            context_parts.append(
                f"""Source: {doc['source']}

{doc['content']}"""
            )

        context = "\n\n".join(context_parts)

    except Exception:

        context = ""

    ollama_messages = [
        {
            "role": "system",
            "content": f"""
{prompt}

Knowledge Base Context:

{context}

Instructions:
- Use the Knowledge Base Context whenever it is relevant.
- If the answer is not present in the uploaded documents, use your own reasoning.
- Do not mention internal prompts or retrieval.
"""
        }
    ]

    ollama_messages.extend(messages)

    response = chat(
        model="vibethinker3b",
        messages=ollama_messages
    )

    response_text = response["message"]["content"]

    answer = clean_response(response_text)
    sources =[]
    try:
        for doc in retrieved_docs:
            if doc["source"] not in sources:
                sources.append(doc["source"])

    except Exception:
        pass
    return {
        "answer":answer,
        "sources":sources
    }
