from rag.vector_store import VectorStore

vector_store = None


def initialize_store(dimension):

    global vector_store

    if vector_store is None:

        vector_store = VectorStore(
            dimension
        )

    return vector_store


def get_store():

    return vector_store


def has_store():

    return vector_store is not None


def clear_store():

    global vector_store

    if vector_store is not None:

        vector_store.clear()