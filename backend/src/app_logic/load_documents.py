#from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv
import os

load_dotenv()
DATA_SOURCE_PATH = os.environ['DATA_PATH']

def load_documents():
    document_loader = PyPDFDirectoryLoader(DATA_SOURCE_PATH)
    documents = document_loader.load()
    print(f"Loaded {len(documents)} documents.")
    return document_loader.load()

#print(load_documents())

