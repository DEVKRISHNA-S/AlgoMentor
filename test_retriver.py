from app.RAG.retriever import retrieve

results = retrieve(
    "How does binary search work?"
)

print(results[0])