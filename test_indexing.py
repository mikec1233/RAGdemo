from dotenv import load_dotenv
import os
from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader
from api.app.components.pipeline.pipeline_component import PipelineComponentFactory
from api.app.components.client.client_component import ClientFactory
from llama_index.vector_stores.opensearch import (
    OpensearchVectorStore,
    OpensearchVectorClient,
)
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.ingestion import IngestionPipeline
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor

# Load environment variables
load_dotenv()
files = os.getenv('DATA_PATH')

# Load documents
documents = SimpleDirectoryReader(input_dir=files, recursive=True).load_data()

# Initialize OpenSearch vector client
client_factory = ClientFactory(
    endpoint="http://localhost:9200",
    index="ragdemo",
    dim=1536,
    embedding_field="embedding",
    text_field="content",
)
client = client_factory.create_client()
vector_store = OpensearchVectorStore(client=client)

# Define and run ingestion pipeline
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=1024, chunk_overlap=50),
        OpenAIEmbedding(model="text-embedding-3-large"),
    ]
)
nodes = pipeline.run(documents=documents)

print(pipeline.transformations)
print(vector_store)

vector_store.add(nodes=nodes)


