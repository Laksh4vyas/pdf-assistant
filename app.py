import streamlit as st
import tempfile
import os
from utils import extract_text_from_pdf, split_text, create_faiss_index, answer_query

st.set_page_config(page_title="GenAI PDF Assistant", layout="wide")
st.title("📄 GenAI PDF Q&A Assistant")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    if "index" not in st.session_state:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_path = tmp_file.name
        with st.spinner("Processing PDF..."):
            text = extract_text_from_pdf(temp_path)
            st.session_state.chunks = split_text(text)
            st.session_state.index = create_faiss_index(st.session_state.chunks)
        os.remove(temp_path)
        st.success("PDF Processed Successfully ✅")

    query = st.text_input("Ask your question:")
    if query:
        with st.spinner("Generating answer..."):
            answer = answer_query(query, st.session_state.chunks, st.session_state.index)
        st.subheader("Answer:")
        st.write(answer)