from llama_index.core.ingestion import IngestionPipeline
from llama_index.core import Settings
from typing import List, Optional
from llama_index.vector_stores.opensearch import OpensearchVectorStore

## https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/ ##
## This is just boiler plate code from LLamaindex docs, just here as placeholder for later ##


class PipelineComponentFactory:
    def __init__(self, project_name:str):
        self.project_name = project_name

    def createPipeline(self,vector_store:OpensearchVectorStore) -> IngestionPipeline:
        return IngestionPipeline(
            project_name= self.project_name,
            transformations=self.transformations,
            vector_store = vector_store,
        )
