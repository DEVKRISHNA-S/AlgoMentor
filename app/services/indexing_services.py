from services.document_loader import load_document
from services.chunking_service import chunk_text

from rag.embedder import get_embedding
from rag.vector_store_manager import initialize_store


def process_document(file_path):

    text = load_document(file_path)

    chunks = chunk_text(text)

    if len(chunks) == 0:
        return 0

    embeddings = []

    for chunk in chunks:

        embeddings.append(
            get_embedding(chunk)
        )

    store = initialize_store(
        len(embeddings[0])
    )

    store.add_chunks(
        chunks,
        embeddings
    )

    return len(chunks)