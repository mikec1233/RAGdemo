from langchain_community.document_loaders import DirectoryLoader
from dotenv import load_dotenv
import os

load_dotenv()
DATA_PATH = os.environ['DATA_PATH']

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*md")
    documents = loader.load()
    return documents

print(load_documents())

