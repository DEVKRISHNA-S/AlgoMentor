from pathlib import Path

from rag.vector_store_manager import get_store


UPLOAD_DIR = Path("uploads")


def delete_document(source):

    store = get_store()

    if store is None:
        return

    store.delete_document(source)

    file_path = UPLOAD_DIR / source

    if file_path.exists():
        file_path.unlink()


def clear_knowledge_base():

    store = get_store()

    if store is not None:
        store.clear()

    if UPLOAD_DIR.exists():

        for file in UPLOAD_DIR.iterdir():

            if file.is_file():
                file.unlink()