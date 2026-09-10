# DocSense_AI

A Python-based Retrieval-Augmented Generation (RAG) application that ingests PDF, DOCX, and TXT documents, generates semantic embeddings using Hugging Face Sentence Transformers, stores them in a Chroma Vector Database, and enables context-aware question answering with source citations.

---

## Overview

The Multi-Document AI Knowledge Assistant is designed to provide intelligent question answering over multiple documents using a Retrieval-Augmented Generation (RAG) pipeline. Instead of relying solely on the knowledge of a language model, the application retrieves relevant information from uploaded documents and uses that context to generate accurate and grounded responses.

The project demonstrates the complete lifecycle of a RAG application, including document ingestion, text preprocessing, embedding generation, vector storage, semantic retrieval, prompt construction, and LLM integration.

---

## Features

- Supports multiple document formats (PDF, DOCX, TXT)
- Automatic document loading and preprocessing
- Semantic text chunking using Recursive Character Text Splitter
- Embedding generation using Hugging Face Sentence Transformers
- Chroma Vector Database integration
- Retrieval-Augmented Generation (RAG)
- Context-aware question answering
- Source-aware responses
- Modular architecture
- Easily extendable with different LLMs and vector databases

---

## Resume Description

Built a modular Retrieval-Augmented Generation (RAG) assistant using Python, LangChain, Hugging Face Sentence Transformers, and ChromaDB to ingest PDFs, DOCX, and TXT documents, perform semantic retrieval, and generate context-aware answers with document citations.

---

## Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | LangChain |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| Document Processing | PyPDF, Python-Docx |
| Environment Management | python-dotenv |
| LLM | Configurable (Groq/OpenAI/Ollama/Hugging Face) |

---

## Project Structure

```text
Multi-Document-AI-Knowledge-Assistant/
│
├── README.md
├── requirements.txt
├── main.py
│
├── input_handler.py
├── loader_factory.py
├── text_splitter.py
├── embedding.py
├── vector_database.py
├── retriever.py
├── prompt_template.py
├── model.py
│
├── tests/
│
├── PLANNING AREA.pdf
└── text.txt
```

---

## Module Description

| Module | Responsibility |
|---------|----------------|
| main.py | Controls the complete RAG pipeline from document ingestion to answer generation |
| input_handler.py | Accepts the document path from the user |
| loader_factory.py | Loads PDF, DOCX, and TXT documents |
| text_splitter.py | Splits documents into semantic chunks |
| embedding.py | Generates vector embeddings |
| vector_database.py | Creates and stores the Chroma vector database |
| retriever.py | Retrieves the most relevant document chunks |
| prompt_template.py | Builds the prompt using retrieved context and the user's question |
| model.py | Sends the prompt to the configured language model |

---

## System Architecture

```text
User Documents
(PDF / DOCX / TXT)
        │
        ▼
Document Loader
        │
        ▼
Text Splitter
        │
        ▼
Embedding Model
        │
        ▼
Chroma Vector Database
        │
        ▼
Retriever
        │
        ▼
Prompt Builder
        │
        ▼
Large Language Model
        │
        ▼
Answer with Source Citations
```

---

## Workflow

1. The user provides one or more PDF, DOCX, or TXT documents.
2. The appropriate document loader extracts the document contents.
3. The extracted text is divided into smaller chunks using a Recursive Character Text Splitter.
4. Each chunk is converted into vector embeddings using a Hugging Face Sentence Transformer model.
5. The embeddings are stored and indexed in ChromaDB.
6. The user submits a natural language query.
7. The retriever performs semantic similarity search to identify the most relevant document chunks.
8. Retrieved context and the user's question are combined into a prompt.
9. The configured Large Language Model generates a context-aware answer along with source references.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Multi-Document-AI-Knowledge-Assistant.git
cd Multi-Document-AI-Knowledge-Assistant
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
GROQ_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
HUGGINGFACEHUB_API_TOKEN=your_api_key
```

Only the API key required by the LLM configured in `model.py` is necessary. The Hugging Face embedding model runs locally and does not require an API key.

---

## Running the Application

```bash
python main.py
```

When prompted:

```text
Enter your Path:
```

Provide the path to a supported document.

Example:

```text
documents/SAP_APO.pdf
```

---

## Example Questions

- What is SAP APO?
- Summarize the uploaded document.
- Explain the Planning Area concept.
- Compare the uploaded documents.
- List the key concepts discussed in the document.
- Which LLM backend is configured in the application?

---

## Future Enhancements

- Streamlit web interface
- Persistent Chroma storage
- Folder-based document ingestion
- Multiple document upload
- Chat history
- Metadata filtering
- Hybrid search
- Cross-encoder reranking
- Multi-LLM support
- REST API using FastAPI
- Document comparison
- Citation highlighting
