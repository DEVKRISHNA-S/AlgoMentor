# test_retriever.py

from app.rag.retriever import retrieve

results = retrieve(
    "How does binary search work?"
)

print(results[0])