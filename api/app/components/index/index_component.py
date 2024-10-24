from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.schema import Document
from typing import List, Sequence
from llama_index.core.schema import TransformComponent
from llama_index.vector_stores.opensearch import OpensearchVectorStore
from app.components.settings.settings import Settings
from llama_index.core.embeddings import Model
from app.components.embedding.embedding_component import EmbeddingComponent

class IndexingComponent:
    index: VectorStoreIndex


    def __init__(self,vector_store:OpensearchVectorStore, embed_model:EmbeddingComponent, settings:Settings):
        self.vector_store = vector_store
        self.settings = settings
        self.index = VectorStoreIndex.from_vector_store(
            vector_store = vector_store,
            embed_model = EmbeddingComponent.embedding_model
        )