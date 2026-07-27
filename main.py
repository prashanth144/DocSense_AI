
from dotenv import load_dotenv
from input_handler import get_filepath
from loader_factory import get_loader
from text_splitter import splitters
from embedding import embedding_model
from vector_database import vector_Storage
from retriever import retrievers
from langchain_groq import ChatGroq
from prompt_template import creating_template

load_dotenv()
file_path = get_filepath()
loader = get_loader(file_path)
documents = loader.load()
chunk=splitters(documents)
embedding=embedding_model()
vector=vector_Storage(chunk, embedding)
retrive=retrievers(vector)
prompt=creating_template()

llm = ChatGroq(model="openai/gpt-oss-120b", api_key="")

text=input("enter your query")

retrive_docs=retrive.invoke(text)

context=""

for i in retrive_docs:
    context+=i.page_content+"\n\n"


while(True):
    message=prompt.invoke({
    "context":context,
    "question":text
})
response=llm.invoke(message)

print(response.content)

    









 

