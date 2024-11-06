from dotenv import load_dotenv
import os
from llama_index.core import SimpleDirectoryReader
#from api.app.components.client.client_component import ClientComponent
from app.components.client.client_component import ClientComponent
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.vector_stores.opensearch import (
    OpensearchVectorStore,
)
from llama_index.core import VectorStoreIndex, StorageContext
from app.settings.settings import Settings,IndexSettings,LLMSettings,EmbeddingModelSettings,TransformationSettings,RetrieverSettings,ResponseSynthesizerSettings,NodePostProcessingSettings
#from api.app.settings.settings import Settings,IndexSettings,LLMSettings,EmbeddingModelSettings,TransformationSettings
from llama_index.core.node_parser import SentenceSplitter

# Load environment variables
load_dotenv()
files = os.getenv('DATA_PATH')
apikey= os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = apikey

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
        temperature=0.1,
        #settings was missing declaration of api_key
        api_key=apikey
    ),
    embedding=EmbeddingModelSettings(
        model="openai-embedding-3-small",
        dimensions=1536,
        api_key=apikey
    ),
    transformations=TransformationSettings(
        transformations=[
            SentenceSplitter()
        ]
    ),
    retriever=RetrieverSettings(
    index="docdemo",
    similarity_top_k=3,
    ),

    response=ResponseSynthesizerSettings(
    response_mode="context_only"
    ),
    
    nodepostproc=NodePostProcessingSettings(
    post_processors=[
        SimilarityPostprocessor(similarity_cutoff=0.75)
    ]
)
)

# Initialize OpenSearch vector client
client_factory=ClientComponent(settings=settings)
client = client_factory.create_client()


# Load documents -> List[Documents]
print("From dir:" + files)
documents = SimpleDirectoryReader(input_dir=files, recursive=True, required_exts=[".Rmd"]).load_data(show_progress=True)


vector_store = OpensearchVectorStore(client=client)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents=documents,
    storage_context=storage_context,
)

#index= VectorStoreIndex.from_vector_store(vector_store)


