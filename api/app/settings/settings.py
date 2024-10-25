import os
from pydantic import BaseModel, Field
from typing import List
from llama_index.core.schema import TransformComponent
from llama_index.core.node_parser import SentenceSplitter

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
        description="List of transformations to be applied "
    )


class Settings(BaseModel):
    index:IndexSettings
    llm:LLMSettings
    embedding:EmbeddingModelSettings
    transformations:TransformationSettings



global_settings = Settings(
    index=IndexSettings(
        endpoint="http://opensearch:9200",
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
        model="text-embedding-3-large",
        dimensions=1536,
        api_key=os.getenv('OPENAI_API_KEY'),
    ),
    transformations=TransformationSettings(
        transformations=[
            SentenceSplitter()
        ]
    )
)