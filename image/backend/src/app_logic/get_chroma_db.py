from backend.src.app_logic.get_embedding_function import get_embedding_function
from dotenv import load_dotenv
from langchain_chroma import Chroma
import os
import sys
import shutil

load_dotenv()

CHROMA_PATH = os.environ.get("CHROMA_PATH", "data/chroma")
IS_USING_IMAGE_RUNTIME = bool(os.environ.get("IS_USING_IMAGE_RUNTIME", False))

def get_chroma_db():

    # Hack needed for AWS Lambda's base Python image (to work with an updated version of SQLite).
    # In Lambda runtime, we need to copy ChromaDB to /tmp so it can have write permissions.
    if IS_USING_IMAGE_RUNTIME:
        __import__("pysqlite3")
        sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
        copy_chroma_to_tmp()

    # prepare the DB
    global CHROMA_DB_INSTANCE
    CHROMA_DB_INSTANCE = Chroma(
            persist_directory=get_runtime_chroma_path(),
            embedding_function=get_embedding_function(),
        )
    print(f"✅ Init ChromaDB {CHROMA_DB_INSTANCE} from {get_runtime_chroma_path()}")

    return CHROMA_DB_INSTANCE

# only executed if we are in a runtime like docker or lambda
def copy_chroma_to_tmp():
    dst_chroma_path = get_runtime_chroma_path()

    if not os.path.exists(dst_chroma_path):
        os.makedirs(dst_chroma_path)

    tmp_contents = os.listdir(dst_chroma_path)
    if len(tmp_contents) == 0:
        print(f"Copying ChromaDB from {CHROMA_PATH} to {dst_chroma_path}")
        os.makedirs(dst_chroma_path, exist_ok=True)
        shutil.copytree(CHROMA_PATH, dst_chroma_path, dirs_exist_ok=True)
    else:
        print(f"✅ ChromaDB already exists in {dst_chroma_path}")

""" def get_runtime_chroma_path():
    #will probably change when hosting - for now just local
    return CHROMA_PATH """

def get_runtime_chroma_path():
    if IS_USING_IMAGE_RUNTIME:
        # must be the tmp folder because in lambda that is the only place we have wright acces to 
        return f"/tmp/{CHROMA_PATH}"
    else:
        return CHROMA_PATH