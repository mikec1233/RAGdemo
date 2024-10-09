from llama_index.core import VectorStoreIndex, StorageContext
from typing import List

class IndexingComponent:
    def __init__(self, storage_context: StorageContext):
        self.storage_context = storage_context
        self.index = None

    def create_index(self, documents: List[dict]):
        self.index = VectorStoreIndex.from_documents(
            documents=documents,
            storage_context=self.storage_context
        )

    def add_documents(self, documents: List[dict]):
        if self.index is None:
            self.create_index(documents)
        else:
            self.index.add_documents(documents)

    def query_index(self, query_text: str, top_k: int = 5):
        if self.index is None:
            raise ValueError("Index has not been created yet.")
        return self.index.query(query_text, top_k=top_k)