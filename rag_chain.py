# rag_chain.py
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from retriever import get_retriever

def build_rag_chain():
    load_dotenv()
    print("[rag_chain.py] Loading Groq LLM and retriever...")
    llm = ChatGroq(model="llama3-70b-8192", temperature=0.7)
    retriever = get_retriever()
    return llm, retriever



if __name__ == "__main__":
    build_rag_chain()
