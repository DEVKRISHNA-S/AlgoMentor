from ollama import chat


def ask_model(prompt: str):

    response = chat(
        model="vibethinker3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]