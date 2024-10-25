from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.opensearch import OpensearchVectorStore
from app.settings.settings import Settings
from app.components.embedding.embedding_component import EmbeddingComponent

class IndexingComponent:
    index: VectorStoreIndex


    def __init__(self,vector_store:OpensearchVectorStore, settings:Settings):
        self.vector_store = vector_store
        self.settings = settings
        self.index = VectorStoreIndex.from_vector_store(
            vector_store = vector_store,
            embed_model = EmbeddingComponent(settings).embedding_model
        )