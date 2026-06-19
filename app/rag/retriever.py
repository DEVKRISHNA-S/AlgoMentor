import faiss
import numpy as np
from pathlib import Path

from .embedder import get_embedding


INDEX_PATH = "vectorstore/faiss_index"

if not Path(INDEX_PATH).exists():
    raise FileNotFoundError(
        "FAISS index not found. Run build_index.py first."
    )

index = faiss.read_index(INDEX_PATH)

with open(
    "vectorstore/documents.txt",
    "r",
    encoding="utf-8"
) as f:

    docs = f.read().split(
        "\n---DOC_SEPARATOR---\n"
    )


def retrieve(query, k=1):

    query_embedding = get_embedding(query)

    query_embedding = np.array(
        [query_embedding]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        k
    )

    return [
        docs[i]
        for i in indices[0]
        if i < len(docs)
    ]