from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
## Router Imports ##
from app.server.chat.chat_router import chat_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(chat_router)

        # Add CORS middleware
        #IT IS IMPERATIVE THAT WE CHANGE THIS IN PROD
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"], 
        allow_headers=["*"], 
    )


    return app
