from llama_index.core.embeddings import BaseEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding
from app.settings.settings import Settings

class EmbeddingComponent:
    embedding_model: BaseEmbedding

    def __init__(self,settings: Settings) -> None:
        self.embedding_model = OpenAIEmbedding(
            model=settings.embedding.model,
            dimensions=settings.embedding.dimensions,
        )