from langchain_core.prompts import ChatPromptTemplate

def creating_template():
    Prompt=ChatPromptTemplate.from_template(
        template="""
    You are an helpful AI assistant.
    Use only the provided Context to answer

    Context:{context}
    Question:{question}
"""
        
    )
    return Prompt
