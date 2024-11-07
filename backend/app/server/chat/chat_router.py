from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.server.chat.chat_service import ChatService


chat_router = APIRouter(prefix="/v1")
chat_service = ChatService()

class QueryRequest(BaseModel):
    user_input: str

@chat_router.post("/chat/query", response_model=dict)
async def query_chat(request: QueryRequest):
    try:
        # Call the query method from ChatService
        response = chat_service.query(request.user_input)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))