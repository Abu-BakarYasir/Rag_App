import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load env
load_dotenv()
CHROMA_DIR = "db/chroma_react"
PDF_PATH = os.path.expanduser("~/Downloads/ReactJSNotesForProfessionals.pdf")

# Check or create vector store
if not os.path.exists(CHROMA_DIR):
    with st.spinner("Embedding PDF & building vector DB..."):
        loader = PyPDFLoader(PDF_PATH)
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        vectordb = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=CHROMA_DIR)
        vectordb.persist()

# Load model and retriever
llm = ChatGroq(model="llama3-70b-8192", temperature=0)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
retriever = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings).as_retriever()

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type="stuff"
)

# Streamlit UI
st.set_page_config(page_title="📘 ReactJS RAG QA", layout="centered")
st.title("📘 Ask Questions About ReactJS Book")

query = st.text_input("Ask a question from the PDF:", placeholder="e.g., What is JSX?")
if query:
    with st.spinner("Searching..."):
        result = qa_chain.invoke({"query": query})

        st.subheader("📤 Answer:")
        st.write(result["result"])

        st.markdown("---")
        st.subheader("📚 Context used from PDF:")
        for i, doc in enumerate(result["source_documents"]):
            with st.expander(f"Chunk {i+1}"):
                st.markdown(doc.page_content)
