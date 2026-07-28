from dotenv import load_dotenv

import retriever
load_dotenv()
from input_handler import input_path
from loader_factory import input_loader
from text_splitter import get_textsplitter
from embedding import get_embeddings
from vector_database import get_vectorspace
from retriever import get_retrievers
from prompt_template import get_prompt
from model import get_model


path=input_path()
loaders=input_loader(path)
documents=loaders.load()
chunking=get_textsplitter(documents)
embedding=get_embeddings()
vectors=get_vectorspace(chunking,embedding)
retriver=get_retrievers(vectors)
llm_model=get_model()
prompt=get_prompt()


while True:

    text = input("Enter your query: ")

    if text.lower() == "exit":
        print("Goodbye!")
        break

    docs = retriver.invoke(text)

    context = ""

    for i in docs:
        context += i.page_content + "\n\n"

    message = prompt.invoke({
        "context": context,
        "question": text
    })

    response = llm_model.invoke(message)
    print(response.content)

