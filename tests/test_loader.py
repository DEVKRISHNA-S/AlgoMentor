from app.services.document_loader import (
    load_document
)

print(
    load_document(
        "data/binary_search.md"
    )[:500]
)