# retriever.py
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_DIR = "db/chroma_react"

def get_retriever():
    print("[retriever.py] Loading Chroma vector DB...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vectorstore = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    print("[retriever.py] Vector DB loaded.")
    return vectorstore.as_retriever()

if __name__ == "__main__":
    retriever = get_retriever()
    docs = retriever.get_relevant_documents("What is JSX?")
    print("[retriever.py] Retrieved", len(docs), "docs")
