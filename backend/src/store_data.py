import chromadb
from dotenv import load_dotenv
import os
import openai
import shutil
from langchain_openai import OpenAIEmbeddings
#from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from load_documents import load_documents
from split_documents import split_text
from langchain.schema import Document
load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']
CHROMA_PATH = os.environ['CHROMA_PATH']

#data_path = os.environ["DATA_PATH"]
#client = chromadb.PersistentClient(path="CHROMA_PATH")

'''Basic implementaion -- just repopulating Chroma database everytime we run... will be changed to check if split docs are already there
'''

documents = load_documents()
chunks = split_text(documents)

def save_to_chroma(chunks: list[Document]):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new DB from the documents.
    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )
    #db.persist()
    #perist method removed, docs are automatically persisted
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

save_to_chroma(chunks)