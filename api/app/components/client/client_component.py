from llama_index.vector_stores.opensearch import OpensearchVectorClient
from api.app.components.settings.settings import Settings

class ClientComponent:
    endpoint: str
    index: str
    dim: int
    embedding_field: str
    text_field: str
    
    def __init__(self, settings: Settings) -> None:
        self.endpoint = settings.index.endpoint
        self.index = settings.index.index
        self.dim = settings.index.dim
        self.embedding_field = settings.index.embedding_field
        self.text_field = settings.index.text_field

    def create_client(self):
        client = OpensearchVectorClient(
            endpoint=self.endpoint,
            index=self.index,
            dim=self.dim,
            embedding_field=self.embedding_field,
            text_field=self.text_field
        )
        return client