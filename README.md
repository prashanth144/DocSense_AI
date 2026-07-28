# DocScense_AI

A Python-based multi-document AI knowledge assistant that ingests PDFs/TXT/DOCX, splits and embeds their text, stores embeddings in a Chroma vector store, and answers user queries with source-aware context (chat-style Q&A with document citations). Built for exploratory question answering over collections of documents — useful for knowledge-base search, research assistants, and document comparison.

Built a Python document-QA assistant using LangChain, HuggingFace sentence-transformers, and Chroma to ingest, chunk, embed, and retrieve multi-document context for LLM-backed question answering with source citations.

**Stack**
Language: Python 

Framework : LangChain 

Libraries:  langchain
            langchain-huggingface
            sentence-transformers
            langchain-chroma
            pypdf ,python-docx
            python-dotenv

**How it's organized**

**Code**

README.md                project summary
requirements.txt         Python dependencies
main.py                  orchestrates ingestion → embedding → retrieval → LLM answering (CLI loop)
input_handler.py         reads user-provided file path
loader_factory.py        selects a document loader (PDF / TXT / DOCX) using langchain_community loaders
text_splitter.py         chunks documents (RecursiveCharacterTextSplitter)
embedding.py             creates HuggingFaceEmbeddings (sentence-transformers/all-MiniLM-L6-v2)
vector_database.py       builds a Chroma vectorstore from chunks + embeddings
retriever.py             (retrieval logic — returns relevant document chunks)
prompt_template.py       (builds the prompt using retrieved context and question)
model.py                 (wraps / invokes the LLM to generate answers)
tests/                   test directory (empty / placeholder)
PLANNING AREA.pdf        project plan / documentation asset
text.txt                 example or test text


main.py is the entry point: it asks for a path, uses loader_factory to load documents, text_splitter to chunk them, embedding.py to compute embeddings, vector_database.py to create a Chroma vector store, and retriever to fetch relevant chunks for a query. prompt_template builds the context+question prompt, and model.py sends it to an LLM to produce an answer which is printed to the console.

**How to run it**

Create and activate a virtual env (recommended).
Install dependencies and run main.py.

**Example commands:**

**Code**
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py

The app uses python-dotenv (load_dotenv()), so add a .env file in the repo root if your LLM/provider requires API keys (e.g., HUGGINGFACE_HUB_TOKEN, OPENAI_API_KEY). The code uses a local Hugging Face sentence-transformers model for embeddings (sentence-transformers/all-MiniLM-L6-v2), and Chroma for the vector DB; a remote LLM provider may still require provider keys in model.py.

When running, the CLI prompts "Enter your Path" — give a path to a .pdf, .txt, or .docx document.

