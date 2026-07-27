from langchain_community.document_loaders import(
    PyPDFLoader,
    textloader,
    UnstructuredWordDocumentLoader
)

def get_loader(file_path):
    file_extension = file_path.suffix.lower()
    
    if file_extension == ".pdf":
        return PyPDFLoader(file_path)
    elif file_extension == ".docx":
        return UnstructuredWordDocumentLoader(file_path)
    elif file_extension == ".txt":
        return textloader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")