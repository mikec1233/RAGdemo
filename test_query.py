from api.app.components.client.client_component import ClientComponent
from llama_index.vector_stores.opensearch import (
    OpensearchVectorStore,
)
from llama_index.core import VectorStoreIndex
from api.app.components.settings.settings import Settings,IndexSettings,LLMSettings,EmbeddingModelSettings


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
    ),
    embedding=EmbeddingModelSettings(
        model="openai-embedding",
        dimensions=512,
    )
)

# Initialize OpenSearch vector client
client_factory=ClientComponent(settings=settings)
client = client_factory.create_client()

vector_store = OpensearchVectorStore(client=client)

index = VectorStoreIndex.from_vector_store(vector_store)

query_engine = index.as_query_engine()

# Perform a query
res = query_engine.query("What functions should I use for date and datetime imputations")
print(res)
