from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv

load_dotenv()

def embedding_model():
    model=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2")
    return model






