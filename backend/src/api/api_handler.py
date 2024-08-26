import os
import uvicorn
import json
from fastapi import FastAPI
from pydantic import BaseModel
from backend.src.database.db_model import DBQueryModel

from backend.src.app_logic.query_data import query_rag


app = FastAPI()

class SubmitQueryRequest(BaseModel):
    query_text: str

@app.get("/")
def index():
    return{"Hello": "World"}

@app.get("/get_query")
def get_query_endpoint(query_id: str) -> DBQueryModel:
    query = DBQueryModel.get_item(query_id)
    return query

@app.post("/submit_query")
def submit_query_endpoint(request: SubmitQueryRequest) -> DBQueryModel:
    new_query = DBQueryModel(query_text=request.query_text)
    # Make a synchronous call to the worker (the RAG/AI app).
    query_response = query_rag(request.query_text)
    new_query.answer_text = query_response.response_text
    new_query.sources = query_response.sources
    new_query.is_complete = True
    new_query.put_item()

    return new_query


if __name__ == "__main__":
    # Run this as a server directly.
    port = 8000
    print(f"Running the FastAPI server on port {port}.")
    uvicorn.run("__main__:app", host="0.0.0.0", port=port)





