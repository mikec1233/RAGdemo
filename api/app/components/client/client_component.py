from llama_index.vector_stores.opensearch import OpensearchVectorClient
from typing import Tuple

class ClientFactory:
    def __init__(self, endpoint:str, index:str, dim:int, embedding_field:str, text_field:str):
        self.endpoint = endpoint
        self.index = index
        self.dim = dim
        self.embedding_field = embedding_field
        self.text_field = text_field

    def create_client(self):
        client = OpensearchVectorClient(
            endpoint = self.endpoint,
            index = self.index,
            dim = self.dim,
            embedding_field = self.embedding_field,
            text_field = self.text_field
        )
        return client
