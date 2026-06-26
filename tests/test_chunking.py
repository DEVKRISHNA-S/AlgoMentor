from app.services.chunking_service import (
    chunk_text
)

sample_text = (
    "Binary Search " * 200
)

chunks = chunk_text(
    sample_text
)

print(
    f"Chunks: {len(chunks)}"
)

print(
    chunks[0]
)