from typing import Union
from fastapi import FastAPI, HTTPException
from opensearchpy import OpenSearch

app = FastAPI()

## These are just boilerplate functions I copied from FastAPI docs, placeholder feel free to remove #
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}




## TEST FUNCTION TO PING OPENSEARCH DATABASE ###
OPENSEARCH_HOST = "http://opensearch:9200" 
client = OpenSearch(hosts=[OPENSEARCH_HOST])
@app.get("/ping")
async def pingToDB():
    try:
        response = client.ping()
        if response:
            return {"status": "success", "message": "Connected to OpenSearch!"}
        else:
            raise HTTPException(status_code=503, detail="Failed to connect to OpenSearch.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
