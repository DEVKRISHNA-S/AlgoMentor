from rag.vector_store_manager import get_store


def get_dashboard_data():

    store = get_store()

    if store is None:

        return {
            "documents": 0,
            "chunks": 0,
            "sources": [],
            "ready": False
        }

    sources = []

    for doc in store.documents:

        if doc["source"] not in sources:

            sources.append(
                doc["source"]
            )

    return {

        "documents": store.total_documents(),

        "chunks": store.total_chunks(),

        "sources": sources,

        "ready": True
    }