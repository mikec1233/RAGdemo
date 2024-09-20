import argparse
from dotenv import load_dotenv
import os
from dataclasses import dataclass
from typing import List
#from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from backend.src.app_logic.get_chroma_db import get_chroma_db

load_dotenv()

#CHROMA_PATH = os.environ['CHROMA_PATH']

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

OPENAI_MODEL_ID = "gpt-3.5-turbo-0125"

@dataclass

class QueryResponse:
    query_text: str
    response_text: str
    sources: List[str]

def query_rag(query_text: str) -> QueryResponse:
    db = get_chroma_db()
    results = db.similarity_search_with_relevance_scores(query_text, k=3) 
    
    #check if results are suitable
    if len(results) == 0 or results[0][1] < 0.7:
        print(f"Unable to find matching results.")
        #When no results are found we return, however we are not returning a QueryResponse object.
        #To fix this we are going to are going to return a QueryResponse object with the statement "No suitable results found"
        return QueryResponse(query_text=query_text, response_text="No suitable results found.", sources=[])
    
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    model = ChatOpenAI(model=OPENAI_MODEL_ID)
    response = model.invoke(prompt)
    response_text = response.content
    sources = [doc.metadata.get("id", "Unknown") for doc, _score in results]
    print(f"Response: {response_text})\nSources: {sources}")

    return QueryResponse(
        query_text=query_text, response_text=response_text, sources=sources
    )


# def main():
#     # Create CLI.
#     parser = argparse.ArgumentParser()
#     parser.add_argument("query_text", type=str, help="The query text.")
#     args = parser.parse_args()
#     query_text = args.query_text

    # Prepare the DB.
    #embedding_function = OpenAIEmbeddings()
    #db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    #results = db.similarity_search_with_relevance_scores(query_text, k=3)
    # if len(results) == 0 or results[0][1] < 0.7:
    #     print(f"Unable to find matching results.")
    #     return
    
    # context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    # prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    # prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)

    # model = ChatOpenAI(model=OPENAI_MODEL_ID)
    # response_text = model.invoke(prompt)

    # sources = [doc.metadata.get("source", None) for doc, _score in results]
    # formatted_response = f"Response: {response_text}\nSources: {sources}"
    # print(formatted_response)
    


# if __name__ == "__main__":
#     main()