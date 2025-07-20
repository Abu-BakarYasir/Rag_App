# loader.py
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_docs(pdf_path):
    print("[loader.py] Loading PDF:", pdf_path)
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    print(f"[loader.py] Loaded {len(docs)} pages.")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    print(f"[loader.py] Split into {len(chunks)} chunks.")
    return chunks



if __name__ == "__main__":
    test_path = os.path.expanduser("~/Downloads/ReactJSNotesForProfessionals.pdf")
    load_and_split_docs(test_path)