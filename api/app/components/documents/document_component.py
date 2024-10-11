from llama_index.core import SimpleDirectoryReader
from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.core.schema import BaseNode
from typing import Sequence, List

class DocumentComponent:
    def __init__(self, input_files:List):
        self.input_files = input_files

    def load_documents(self) -> List[Document]:
        return SimpleDirectoryReader(input_files=self.input_files)
    

