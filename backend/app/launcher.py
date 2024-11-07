from fastapi import FastAPI
## Router Imports ##
from app.server.chat.chat_router import chat_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(chat_router)


    return app
