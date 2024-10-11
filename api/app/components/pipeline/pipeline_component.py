from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.core.schema import BaseNode
from typing import Sequence, List

## https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/ ##
## This is just boiler plate code from LLamaindex docs, just here as placeholder for later ##


class PipelineComponentFactory:
    def __init__(self, project_name:str, transformations:List):
        self.transformations = transformations
        self.project_name = project_name
    
    def createPipeline(self,name:str) -> IngestionPipeline:
        return IngestionPipeline(
            name = name,
            project_name = self.project_name,
            transformations = self.transformations,
        )
        
