from app.components.index.index_component import IndexingComponent
from app.components.client.client_component import ClientComponent
from llama_index.vector_stores.opensearch import OpensearchVectorStore, OpensearchVectorClient
from llama_index.core import VectorStoreIndex
from llama_index.core.base import base_query_engine
from app.settings.settings import Settings, global_settings


class ChatService:
    def __init__(self) -> None:
        self.client=ClientComponent(global_settings).create_client()
        self.vector_store=OpensearchVectorStore(self.client)
        self.index=IndexingComponent(vector_store=self.vector_store,settings=global_settings).index
        self.query_engine=self.index.as_query_engine()

    def query(self, user_input: str) -> dict:
            query_result = self.query_engine.query(user_input)
            #return query_result
            return {"response": query_result.response}
    
