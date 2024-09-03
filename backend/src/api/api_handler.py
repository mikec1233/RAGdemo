import os
import uvicorn
import json
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.src.database.db_model import DBQueryModel

from backend.src.app_logic.query_data import query_rag

CHARACTER_LIMIT = 2000
app = FastAPI()


class SubmitQueryRequest(BaseModel):
    query_text: str
    user_id: Optional[str] = None

# @app.get("/")
# def index():
#     return{"Hello": "World"}

@app.get("/get_query")
def get_query_endpoint(query_id: str) -> DBQueryModel:
    query = DBQueryModel.get_item(query_id)
    if query:
        return query
    else:
        raise HTTPException(status_code=404, detail=f"Query Not Found: {query_id}")

@app.post("/submit_query")
def submit_query_endpoint(request: SubmitQueryRequest) -> DBQueryModel:
    if len(request.query_text) > CHARACTER_LIMIT:
        raise HTTPException(status_code=400, detail=f"Query is too long. Character limit is: {CHARACTER_LIMIT}")
    

    #new_query = DBQueryModel(query_text=request.query_text)
    user_id = request.user_id if request.user_id else "unknown"
    new_query = DBQueryModel(query_text=request.query_text, user_id=user_id) 

    # Make a synchronous call to the worker (the RAG/AI app).
    query_response = query_rag(request.query_text)
    new_query.answer_text = query_response.response_text
    new_query.sources = query_response.sources
    new_query.is_complete = True
    new_query.put_item()

    return new_query

@app.post("/list_queries")
def list_query_endpoint(user_id: str) -> list[DBQueryModel]:
    ITEM_COUNT = 5
    print(f"Printing Quries for user: ${user_id}")
    query_items = DBQueryModel.list_queries_by_user(user_id=user_id, count=ITEM_COUNT)
    return query_items

if __name__ == "__main__":
    # Run this as a server directly.
    port = 8000
    print(f"Running the FastAPI server on port {port}.")
    uvicorn.run("__main__:app", host="0.0.0.0", port=port)





