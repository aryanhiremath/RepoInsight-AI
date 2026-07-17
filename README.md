# RepoInsight-AI


## ✨ Features
..
* **GitHub Repository Analysis** – Analyze any public GitHub repository by simply pasting its URL.
* **Automatic Repository Cloning** – Securely clones the repository and prepares it for analysis.
* **Smart Code Parsing** – Extracts and processes source code, configuration files, and documentation while ignoring unnecessary files.
* **Semantic Search with FAISS** – Creates vector embeddings of the repository and stores them in a FAISS vector database for efficient retrieval.
* **AI-Powered Repository Chat** – Ask natural language questions about the codebase and receive context-aware answers.
* **File-Aware Responses** – Every answer includes references to the relevant files used to generate the response.
* **Automatic Repository Summary** – Generates a concise overview of the project's purpose, architecture, technologies, and folder structure.
* **Local AI Inference** – Runs entirely with Ollama and Hugging Face models, eliminating the need for paid API keys.

GitHub Repository URL
|
↓
Repository Cloning
|
↓
Source File Extraction
|
↓
Document Loading
|
↓
Text Chunking
|
↓
Embedding Generation
(Ollama - nomic-embed-text)
|
↓
FAISS Vector Database
|
↓
Retriever
|
↓
Local LLM
(Ollama - Qwen)
|
↓
Repository Q&A


---

## 🛠️ Tech Stack

### AI / ML
- LangChain
- Ollama
- FAISS
- RAG Architecture
- Embeddings

### Backend
- Python

### Repository Processing
- Git
- pathlib

### Models
- **nomic-embed-text** – Embedding model
- **qwen2.5** – Local LLM

---

## 🚀 How It Works

1. User provides a GitHub repository URL.
2. RepoInsight clones the repository.
3. Relevant source files are extracted.
4. Files are converted into documents.
5. Documents are split into smaller chunks.
6. Embeddings are generated for each chunk.
7. FAISS stores the vector representations.
8. User asks questions about the repository.
9. Relevant context is retrieved from the vector database.
10. Local LLM generates answers based on the repository content.

---

## 📂 Project Structure
RepoInsight-AI/
│
├── main.py # Application entry point
├── clone_repo.py # GitHub repository cloning
├── ingest.py # File extraction and document loading
├── chunker.py # Document chunking
├── embeddings.py # Embedding generation and FAISS storage
├── rag.py # Retrieval-Augmented Generation pipeline
│
├── repos/ # Cloned repositories
│
└── pyproject.toml



---

## 🔮 Future Improvements

- FastAPI backend integration
- React frontend dashboard
- Persistent FAISS indexes
- Repository architecture visualization
- Automatic project summary generation
- Chat history support
- Cloud deployment

---

## 📌 Current Status

✅ GitHub repository ingestion completed  
✅ Document processing pipeline completed  
✅ Text chunking implemented  
✅ Ollama embedding integration completed  
✅ FAISS vector search implemented  
✅ RAG-based repository Q&A completed  

Frontend and API integration are planned for the next phase