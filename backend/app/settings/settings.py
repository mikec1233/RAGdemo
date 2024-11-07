import os
from pydantic import BaseModel, Field
from typing import List
from llama_index.core.schema import TransformComponent
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.vector_stores.types import MetadataFilters
from llama_index.core.postprocessor.types import BaseNodePostprocessor
from llama_index.core.postprocessor import SimilarityPostprocessor


### INDEX SETTINGS ####
class IndexSettings(BaseModel):
    endpoint: str = Field(
        description="Http endpoint for connection to database",
    )
    index: str = Field(
        description="Name of index, will create index with name given if one is not found",
    )
    dim: int = Field(
        description="Dimensions of vector store of given index",
    )
    embedding_field: str = Field(
        description="Name of the field in the index to store embedding array in",
        default="embedding",
    )
    text_field: str = Field(
        description="Name of the field to grab text from",
        default="content",
    )


### LLM SETTINGS ###
class LLMSettings(BaseModel):
    model: str = Field(
        description="Name of LLM Model used"
    )
    temperature: float = Field(
        description="temp of LLM, i.e how much it will hallucinate"
    )
    api_key: str = Field(
        description="API key from OPENAI"
    )


### EMBEDDING MODEL SETTINGS ###
class EmbeddingModelSettings(BaseModel):
    model: str = Field(
        description="Name of embedding model"
    )
    dimensions: int = Field(
        description="dimensions of embedding model"
    )
    api_key: str = Field(
        description="API key from OPENAI"
    )

### TRANSFORMATION SETTINGS ###
class TransformationSettings(BaseModel):
    transformations: List[TransformComponent] = Field(
        description="List of transformations to be applied during ingestion"
    )

### RETRIEVER SETTINGS ###
class RetrieverSettings(BaseModel):
    index: str = Field(
        description = "Name of index nodes will be retrieved from"
    )
    similarity_top_k: int = Field(
        description = "How many nodes will be returned from query"
    )
    filters: List[MetadataFilters] = Field(
        description="List of metadata filters",
        default= None,
    )

### RESPONSE SYNTHESIZER SETTINGS ###
class ResponseSynthesizerSettings(BaseModel):
    response_mode:str = Field(
        description="Defines the form of call to LLM to generate response"
    )


### NODE POST PROCESSING ###
class NodePostProcessingSettings(BaseModel):
    post_processors : List[BaseNodePostprocessor] = Field(
        description= "Post Processing to be applied to retrieved nodes"
    )





class Settings(BaseModel):
    index:IndexSettings
    llm:LLMSettings
    embedding:EmbeddingModelSettings
    transformations:TransformationSettings
    retriever:RetrieverSettings
    response:ResponseSynthesizerSettings
    nodepostproc:NodePostProcessingSettings




global_settings = Settings(
    index=IndexSettings(
        endpoint="http://opensearch:9200",
        #endpoint="http://localhost:9200",
        index="docdemo",
        dim=1536,
        embedding_field="embedding",
        text_field="content",
    ),
    llm=LLMSettings(
        model="gpt-3.5-turbo",
        temperature=0.1,
        api_key=os.getenv('OPENAI_API_KEY'),
    ),
    embedding=EmbeddingModelSettings(
        model="text-embedding-3-small",
        dimensions=1536,
        api_key=os.getenv('OPENAI_API_KEY'),
    ),
    transformations=TransformationSettings(
        transformations=[
            SentenceSplitter()
        ]
    ),
    retriever=RetrieverSettings(
        index="docdemo",
        similarity_top_k=3,
    ),
    response=ResponseSynthesizerSettings(
        #Testing different response modes.
        #response_mode="tree_summarize",

        response_mode="context_only"
    ),
    nodepostproc=NodePostProcessingSettings(
        post_processors=[
            SimilarityPostprocessor(similarity_cutoff=0.1)
        ]
    )
)