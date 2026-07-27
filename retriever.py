from langchain_community.vectorstores import chroma

def get_retrievers(vector):
    retriver=vector.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k":4,
            "fetch_k":1000,
            "lambda_mult":0.5
        }
    )
    return retriver

    
    