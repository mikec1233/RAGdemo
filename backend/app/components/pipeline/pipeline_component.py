from llama_index.core.ingestion import IngestionPipeline
from llama_index.vector_stores.opensearch import OpensearchVectorStore, OpensearchVectorClient
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from app.settings.settings import global_settings
from app.components.client.client_component import ClientComponent

pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=512, chunk_overlap=128),
        OpenAIEmbedding(model=global_settings.embedding.model, api_key=global_settings.embedding.api_key),
    ],
    vector_store=OpensearchVectorStore(client=ClientComponent(global_settings).create_client())
)

