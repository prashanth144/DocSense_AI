from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
load_dotenv()

def get_vectorspace(chunking,embedding):
    database=Chroma.from_documents(
        documents=chunking,
        embedding=embedding
    )
    return database
