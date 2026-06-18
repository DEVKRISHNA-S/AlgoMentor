from pathlib import Path
from ollama import chat


PROMPT_PATH = Path("app/prompts/mentor.txt")

def load_prompt(mode: str):

    if mode == "chat":
        prompt_path = Path("app/prompts/mentor.txt")

    elif mode == "problem_solver":
        prompt_path = Path("app/prompts/problem_solver.txt")

    elif mode == "code_review":
        prompt_path = Path("app/prompts/code_review.txt")

    else:
        prompt_path = Path("app/prompts/mentor.txt")

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()


def clean_response(text: str):

    if "</think>" in text:
        text = text.split("</think>")[-1]

    return text.strip()


def ask_model(messages: str, mode:str):

    prompt = load_prompt(mode)

    ollama_messages = [
    {
        "role": "system",
        "content": prompt
    }
    ]
    ollama_messages.extend(messages)


    response = chat(
        model="vibethinker3b",
        messages=ollama_messages
    )

    response_text = response["message"]["content"]

    return clean_response(response_text)