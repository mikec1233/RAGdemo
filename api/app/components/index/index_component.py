from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.schema import Document
from typing import List, Sequence

class IndexingComponent:
    def __init__(self, storage_context: StorageContext):
        self.storage_context = storage_context
        self.index = None

    def create_index(self, documents: Sequence[Document]):
        self.index = VectorStoreIndex.from_documents(
            documents=documents,
            storage_context=self.storage_context
        )


    def add_document(self, document:Document):
        self.index.insert(document)

    def query_index(self, query_text: str, top_k: int = 5):
        if self.index is None:
            raise ValueError("Index has not been created yet.")
        return self.index.query(query_text, top_k=top_k)