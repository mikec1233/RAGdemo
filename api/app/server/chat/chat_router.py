from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.server.chat.chat_service import ChatService


chat_router = APIRouter(prefix="/v1")
chat_service = ChatService()

class QueryRequest(BaseModel):
    message: str

@chat_router.post("/query")
async def query_chat_service(request: QueryRequest):
    try:
        response = await chat_service.query(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
