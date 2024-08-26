from backend.src.app_logic.get_embedding_function import get_embedding_function
from dotenv import load_dotenv
from langchain_chroma import Chroma
import os

load_dotenv()

CHROMA_PATH = os.environ['CHROMA_PATH']

def get_chroma_db():
    global CHROMA_DB_INSTANCE
    CHROMA_DB_INSTANCE = Chroma(
            persist_directory=get_runtime_chroma_path(),
            embedding_function=get_embedding_function(),
        )
    print(f"✅ Init ChromaDB {CHROMA_DB_INSTANCE} from {get_runtime_chroma_path()}")

    return CHROMA_DB_INSTANCE

def get_runtime_chroma_path():
    #will probably change when hosting - for now just local
    return CHROMA_PATH