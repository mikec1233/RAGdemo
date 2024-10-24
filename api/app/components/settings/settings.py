from pydantic import BaseModel, Field


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


### EMBEDDING MODEL SETTINGS ###
class EmbeddingModelSettings(BaseModel):
    model: str = Field(
        description="Name of embedding model"
    )
    dimensions: int = Field(
        description="dimensions of embedding model"
    )

### TRANSFORMATION SETTINGS----- IMPLEMENT LATER #####
class TransformationSettings(BaseModel):
    model:list


class Settings(BaseModel):
    index:IndexSettings
    llm:LLMSettings
    embedding:EmbeddingModelSettings

