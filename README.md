# 📄 ReactJS PDF QA App (RAG-based)

This is a simple **Retrieval-Augmented Generation (RAG)** app built with **Streamlit**, using:
- **ChromaDB** as the vector store
- **HuggingFace embeddings** for document encoding
- **Groq (LLaMA3-70B)** for language generation

It allows you to ask questions based on the content of a PDF file (like a ReactJS book).

---

## 🚀 Features
- Upload and process PDF files
- Embed and store in local Chroma vector DB
- Ask questions about the content (answers grounded in your data)
- Clean and interactive Streamlit UI

---

## 🧱 Tech Stack

- 🧠 **LLM**: Groq (LLaMA3-70B)
- 📚 **Embeddings**: HuggingFace (e.g., `all-MiniLM-L6-v2`)
- 🧠 **Vector Store**: ChromaDB (local)
- 🖥️ **Frontend**: Streamlit
- 📄 **PDF Handling**: PyMuPDF

---

## 🛠️ Setup

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/react-rag-app.git
cd react-rag-app

# 2. Create virtual environment and activate
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Groq API key to .env
echo "GROQ_API_KEY=your_key_here" > .env

# 5. Run the app
streamlit run app.py
```

---

## 📂 Project Structure

```
.
├── app.py                 # Main Streamlit UI
├── .env                  # API key (not pushed)
├── .gitignore            # Ignored files (env, cache, chroma)
├── requirements.txt      # Required packages
└── README.md             # This file
```

---

## 📌 Screenshots:
<img width="1327" height="634" alt="1" src="https://github.com/user-attachments/assets/7da2fa2b-f0b9-4810-8677-1eb68894eed4" />
<img width="1275" height="580" alt="2" src="https://github.com/user-attachments/assets/6e551a07-2092-4a26-84b3-e4b707661619" />

- Answers are based strictly on PDF context embedded — no hallucinations.
- The vector DB is stored locally at `chroma_react/`.

---

## 🧠 Example Question

> **Q**: What are React Hooks?  
> **A**: Based on your PDF, React Hooks allow functional components to use state and lifecycle features...

---

## 🧑‍💻 Author

Built by [Abu Bakar Yasir](https://github.com/Abu-BakarYasir) — Computer Engineering @ COMSATS + Full Stack Developer 🚀
