from pathlib import Path
import faiss
import numpy as np

from app.rag.embedder import get_embedding


DATA_DIR = Path("data")
INDEX_PATH = "vectorstore/faiss_index"


documents = []
embeddings = []

for file in DATA_DIR.glob("*.md"):

    text = file.read_text(encoding="utf-8")

    documents.append(text)

    embedding = get_embedding(text)

    embeddings.append(embedding)

embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, INDEX_PATH)

print(f"Indexed {len(documents)} documents")

with open(
    "vectorstore/documents.txt",
    "w",
    encoding="utf-8"
) as f:

    for doc in documents:
        f.write(doc)
        f.write("\n---DOC_SEPARATOR---\n")