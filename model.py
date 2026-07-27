from langchain_groq import ChatGroq
def get_model():
    llm=ChatGroq(
    model="openai/gpt-oss-120b", api_key=""
)
    return llm

