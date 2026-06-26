from rag.embedder import get_embedding
from rag.vector_store_manager import get_store


def retrieve(query, k=3):

    store = get_store()

    if store is None:
        return []

    if not query.strip():
        return []

    query_embedding = get_embedding(query)

    return store.search(
        query_embedding,
        k
    )