# app.py
import streamlit as st
from rag_chain import build_rag_chain

st.set_page_config(page_title="ReactJS RAG App")
st.title("📘 ReactJS Notes RAG App")
query = st.text_input("Ask a question about ReactJS:")

if query:
    llm, retriever = build_rag_chain()
    docs = retriever.invoke(query)  
    context = "\n".join(doc.page_content for doc in docs[:3])
    response = llm.invoke(context + "\n" + query)

    st.subheader("Answer")
    st.write(response.content)
