from langchain_text_splitters import RecursiveCharacterTextSplitter

def splitters(docs):
    splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
    )
    chunk=splitter.split_documents(docs)
    return chunk







