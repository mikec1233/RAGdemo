import os
from api.app.components.client.client_component import ClientComponent
from llama_index.vector_stores.opensearch import (
    OpensearchVectorStore,
)
from llama_index.core import VectorStoreIndex, StorageContext
from api.app.components.settings.settings import Settings,IndexSettings,LLMSettings,EmbeddingModelSettings
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.storage.index_store import SimpleIndexStore
from llama_index.core.graph_stores import SimpleGraphStore

key = os.getenv('OPENAI_API_KEY')

#Load Settings -- EVENTUALLY THIS WILL BE LOADED FROM YAML FILE 
settings = Settings(
    index=IndexSettings(
        endpoint="http://localhost:9200",
        index="docdemo",
        dim=1536,
        embedding_field="embedding",
        text_field="content",
    ),
    llm=LLMSettings(
        model="gpt-3.5-turbo",
        temperature=0.1 ,
        api_key = key,
    ),
    embedding=EmbeddingModelSettings(
        model="openai-embedding",
        dimensions=512,
        api_key = key, 
    )
)

# Initialize OpenSearch vector client
client_factory=ClientComponent(settings=settings)
client = client_factory.create_client()

vector_store = OpensearchVectorStore(client=client)

index = VectorStoreIndex.from_vector_store(vector_store)

storage_context = StorageContext.from_defaults(vector_store=vector_store)

test = StorageContext(
    docstore= SimpleDocumentStore(),
    index_store= SimpleIndexStore(),
    vector_stores= OpensearchVectorStore(client),
    graph_store= SimpleGraphStore(),
)

print(storage_context)

print(test.docstore)