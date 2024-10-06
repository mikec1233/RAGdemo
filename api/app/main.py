from typing import Union, List
from fastapi import FastAPI, HTTPException
from opensearchpy import OpenSearch

app = FastAPI()

# OpenSearch configuration
OPENSEARCH_HOST = "http://opensearch:9200"
client = OpenSearch(hosts=[OPENSEARCH_HOST])

# Ping OpenSearch to check the connection
@app.get("/ping")
async def ping_to_db():
    try:
        response = client.ping()
        if response:
            return {"status": "success", "message": "Connected to OpenSearch!"}
        else:
            raise HTTPException(status_code=503, detail="Failed to connect to OpenSearch.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Index a document in OpenSearch
@app.post("/index-document/")
async def index_document(doc_id: str, title: str, content: str):
    try:
        document = {
            "title": title,
            "content": content
        }
        response = client.index(index="my-documents-index", id=doc_id, body=document)
        return {"status": "success", "result": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Search for documents in OpenSearch
@app.get("/search/")
async def search_documents(query: str):
    try:
        body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "content"]
                }
            }
        }
        response = client.search(index="my-documents-index", body=body)
        return {"status": "success", "result": response['hits']['hits']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
