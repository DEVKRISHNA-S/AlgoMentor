import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension):

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(
            dimension
        )

        # Metadata for every chunk
        self.documents = []

        # Embedding for every chunk
        self.embeddings = []

        # Global chunk id
        self.next_chunk_id = 0

    def add_chunks(
        self,
        chunks,
        embeddings,
        source
    ):

        embeddings = np.array(
            embeddings
        ).astype("float32")

        self.index.add(
            embeddings
        )

        for chunk, embedding in zip(
            chunks,
            embeddings
        ):

            self.documents.append(
                {
                    "chunk_id": self.next_chunk_id,
                    "content": chunk,
                    "source": source
                }
            )

            self.embeddings.append(
                embedding
            )

            self.next_chunk_id += 1

    def search(
        self,
        query_embedding,
        k=3
    ):

        if len(self.documents) == 0:
            return []

        query_embedding = np.array(
            [query_embedding]
        ).astype("float32")

        distances, indices = self.index.search(
            query_embedding,
            min(k, len(self.documents))
        )

        results = []

        for i in indices[0]:

            if i < len(self.documents):

                results.append(
                    self.documents[i]
                )

        return results

    # ---------------------------------
    # Index Management
    # ---------------------------------

    def rebuild_index(self):

        self.index = faiss.IndexFlatL2(
            self.dimension
        )

        if len(self.embeddings) == 0:
            return

        embeddings = np.array(
            self.embeddings
        ).astype("float32")

        self.index.add(
            embeddings
        )

    def delete_document(
        self,
        source
    ):

        new_documents = []
        new_embeddings = []

        for doc, embedding in zip(
            self.documents,
            self.embeddings
        ):

            if doc["source"] != source:

                new_documents.append(
                    doc
                )

                new_embeddings.append(
                    embedding
                )

        self.documents = new_documents
        self.embeddings = new_embeddings

        self.rebuild_index()

    def clear(self):

        self.documents = []
        self.embeddings = []

        self.next_chunk_id = 0

        self.index = faiss.IndexFlatL2(
            self.dimension
        )

    # ---------------------------------
    # Dashboard Helpers
    # ---------------------------------

    def total_documents(self):

        return len(
            {
                doc["source"]
                for doc in self.documents
            }
        )

    def total_chunks(self):

        return len(
            self.documents
        )

    def get_sources(self):

        return sorted(
            {
                doc["source"]
                for doc in self.documents
            }
        )

    def get_chunk_count(
        self,
        source
    ):

        return sum(
            1
            for doc in self.documents
            if doc["source"] == source
        )