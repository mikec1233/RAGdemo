from llama_index.vector_stores.opensearch import OpensearchVectorStore, OpensearchVectorClient
from llama_index.core import StorageContext

from typing import List, Any

class VectorStoreComponent:
    def __init__(self, client:OpensearchVectorClient):
        self.vector_store = OpensearchVectorStore(client=client)
        ### THIS LINE DEFAULTS OPENSEARCHVECTORSTORE TO STORAGECONTEXT DEFAULTS ###
        self.storage_context= StorageContext.from_defaults(vector_store=self.vector_store)


