from dotenv import load_dotenv
import os
from llama_index.core import SimpleDirectoryReader
from app.components.client.client_component import ClientComponent
from llama_index.core.ingestion import IngestionPipeline
from llama_index.vector_stores.opensearch import OpensearchVectorStore
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
from app.settings.settings import global_settings, Settings, IndexSettings, LLMSettings, EmbeddingModelSettings, TransformationSettings, RetrieverSettings, ResponseSynthesizerSettings, NodePostProcessingSettings
from llama_index.core.postprocessor import SimilarityPostprocessor

# Load environment variables
load_dotenv()
files = os.getenv('DATA_PATH')
apikey = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = apikey

# Load settings (this can be loaded from a YAML configuration in the future)
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
        api_key=apikey
    ),
    embedding=EmbeddingModelSettings(
        model="text-embedding-3-small",
        dimensions=1536,
        api_key=apikey
    ),
    transformations=TransformationSettings(
        transformations=[
            SentenceSplitter(chunk_size=512, chunk_overlap=128)
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

if __name__ == "__main__":

    # Initialize OpenSearch vector client using ClientComponent
    client_factory = ClientComponent(settings=settings)
    client = client_factory.create_client()

    # Set up the OpensearchVectorStore and the IngestionPipeline
    vector_store = OpensearchVectorStore(client=client)

    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=512, chunk_overlap=128),
            OpenAIEmbedding(model=settings.embedding.model, api_key=settings.embedding.api_key),
        ],
        vector_store=vector_store,
    )

    # Load documents from the specified directory
    print("Loading documents from directory:", files)
    #html files
    documents = SimpleDirectoryReader(input_dir=files, recursive=True, required_exts=[".html"]).load_data(show_progress=True)
    #.Rmd
    #documents = SimpleDirectoryReader(input_dir=files, recursive=True, required_exts=[".Rmd"]).load_data(show_progress=True)

    # Run the pipeline to ingest documents into the vector store
    pipeline.run(documents=documents)
    #caching and par. processing not set up - will be useful later. 

    print("Ingestion completed.")
