from llama_index.vector_stores.opensearch import OpensearchVectorStore, OpensearchVectorClient
from llama_index.core.vector_stores.types import BasePydanticVectorStore
from app.settings.settings import Settings


class VectorStoreComponent:
    vector_store:BasePydanticVectorStore

    def __init__(self, client:OpensearchVectorClient, settings:Settings):
        self.client= client
        self.vector_store=(OpensearchVectorStore(client=client))
    