import chromadb
from dotenv import load_dotenv
import os
import openai
import shutil
from langchain_openai import OpenAIEmbeddings
#from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from backend.src.app_logic.load_documents import load_documents
from backend.src.app_logic.split_documents import split_documents
from backend.src.app_logic.get_embedding_function import get_embedding_function
from langchain.schema import Document
load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']
CHROMA_PATH = os.environ['CHROMA_PATH']
#client = chromadb.PersistentClient(path="CHROMA_PATH")

'''Basic implementaion -- just repopulating Chroma database everytime we run... will be changed to check if split docs are already there
'''
documents = load_documents()
chunks = split_documents(documents)

def save_to_chroma(chunks: list[Document]):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new DB from the documents.
    db = Chroma(
         persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )
    db.add_documents(chunks)
    #db.persist()
    #perist method removed, docs are automatically persisted
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

save_to_chroma(chunks)