from langchain_community.document_loaders import(
    PyPDFLoader,
    TextLoader,
    UnstructuredFileLoader
)

def input_loader(file_name):
    suffix = file_name.suffix.lower()

    if suffix == ".txt":
        return TextLoader(file_name)
    elif suffix == ".pdf":
        return PyPDFLoader(file_name)
    elif suffix == ".docx":
        return UnstructuredFileLoader(file_name)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")






