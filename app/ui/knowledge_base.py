import streamlit as st

from services.file_services import save_uploaded_file
from services.indexing_services import process_document
from services.dashboard_services import get_dashboard_data
from services.document_managment_services import (
    delete_document,
    clear_knowledge_base
)

from rag.vector_store_manager import get_store


def render_knowledge_base():

    st.header("📚 Knowledge Base")

    dashboard = get_dashboard_data()

    store = get_store()

    # ----------------------------------
    # Knowledge Base Status
    # ----------------------------------

    st.subheader("Knowledge Base Status")

    if dashboard["ready"]:
        st.success("Knowledge Base Ready")
    else:
        st.warning("No Knowledge Base Built")

    # ----------------------------------
    # Statistics
    # ----------------------------------

    col1, col2 = st.columns(2)

    col1.metric(
        "Documents",
        dashboard["documents"]
    )

    col2.metric(
        "Chunks",
        dashboard["chunks"]
    )

    # ----------------------------------
    # Uploaded Documents
    # ----------------------------------

    st.subheader("Uploaded Documents")

    if dashboard["sources"]:

        for source in dashboard["sources"]:

            col1, col2 = st.columns([5, 1])

            with col1:

                chunk_count = 0

                if store is not None:

                    chunk_count = store.get_chunk_count(
                        source
                    )

                st.markdown(
                    f"**📄 {source}**"
                )

                st.caption(
                    f"{chunk_count} chunks indexed"
                )

            with col2:

                if st.button(
                    "🗑",
                    key=f"delete_{source}"
                ):

                    delete_document(source)

                    st.success(
                        f"{source} deleted."
                    )

                    st.rerun()

    else:

        st.caption(
            "No uploaded documents."
        )

    st.divider()

    # ----------------------------------
    # Upload Documents
    # ----------------------------------

    uploaded_files = st.file_uploader(
        "Upload Notes",
        type=["pdf", "docx", "md"],
        accept_multiple_files=True
    )

    saved_files = []

    if uploaded_files:

        for file in uploaded_files:

            path = save_uploaded_file(
                file
            )

            saved_files.append(
                path
            )

            st.success(
                f"Uploaded: {path.name}"
            )

        if st.button(
            "Build Knowledge Base"
        ):

            total_chunks = 0

            progress = st.progress(0)

            for i, path in enumerate(saved_files):

                total_chunks += process_document(
                    path
                )

                progress.progress(
                    (i + 1) / len(saved_files)
                )

            progress.empty()

            st.success(
                f"Knowledge Base Built Successfully!\n\nIndexed {total_chunks} chunks."
            )

            st.rerun()

    st.divider()

    # ----------------------------------
    # Knowledge Base Actions
    # ----------------------------------

    st.subheader(
        "Knowledge Base Actions"
    )

    if st.button(
        "🗑 Clear Knowledge Base"
    ):

        clear_knowledge_base()

        st.success(
            "Knowledge Base Cleared."
        )

        st.rerun()