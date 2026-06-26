# test_model.py

from app.llm.ollama_client import ask_model

response = ask_model(
    "leetcode 53 maximum subarray"
)

print(response)