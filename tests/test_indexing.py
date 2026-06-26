from app.services.indexing_services import (
    process_document
)

chunks = process_document(
    "data/binary_search.md"
)

print(
    f"Chunks: {len(chunks)}"
)

print(chunks[0])