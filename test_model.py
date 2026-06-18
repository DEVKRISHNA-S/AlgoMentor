# test_model.py

from app.llm.ollama_client import ask_model

response = ask_model(
    "Explain binary search in simple terms."
)

print(response)