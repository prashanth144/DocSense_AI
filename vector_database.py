from langchain_community.vectorstores import Chroma


def vector_Storage(documents, model):
    vector = Chroma.from_documents(
        documents=documents,
        embedding=model,
    )
    return vector