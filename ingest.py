# ingest.py
import os
from loader import load_and_split_docs
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

PDF_PATH = os.path.expanduser("~/Downloads/ReactJSNotesForProfessionals.pdf")
CHROMA_DIR = "db/chroma_react"

def ingest():
    print("[ingest.py] Loading & splitting PDF...")
    docs = load_and_split_docs(PDF_PATH)

    print("[ingest.py] Embedding & storing to Chroma...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    Chroma.from_documents(docs, embedding=embeddings, persist_directory=CHROMA_DIR).persist()
    print("[ingest.py] Ingestion complete. Vector DB saved.")

if __name__ == "__main__":
    ingest()
