from app.components.index.index_component import IndexingComponent
from app.components.client.client_component import ClientComponent
from llama_index.vector_stores.opensearch import OpensearchVectorStore, OpensearchVectorClient
from llama_index.core import VectorStoreIndex
from llama_index.core.base import base_query_engine
from app.settings.settings import Settings, global_settings


class ChatService:
    def __init__(self):
        print("Hello, World! from ChatService")

    async def query(self, message: str) -> str:
        print("Hello, World! from query method")
        return "Hello, World!"
    
    ClientComponent(global_settings)
    
