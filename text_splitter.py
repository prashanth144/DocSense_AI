from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_textsplitter(documents):
    text=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)
    chunk=text.split_documents(documents)
    return chunk
    
