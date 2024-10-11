from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.core.schema import BaseNode
from typing import Sequence, List

class IngestComponent:
    def __init__(self, pipeline:IngestionPipeline):
        self.pipeline = pipeline

    def ingest(self, documents:List[Document]) -> Sequence[BaseNode]:
        return self.pipeline.run(documents=documents)
    