from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.core import SimpleDirectoryReader
import os

# fetch api key from local enviorment
local_api_key = os.getenv("OPENAI_API_KEY")

# load documents 
reader = SimpleDirectoryReader(input_dir = "data")
loaded_docs = reader.load_data()

# create the pipeline with transformations
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size = 25, chunk_overlap = 0),
        TitleExtractor(),
        OpenAIEmbedding(api_key = local_api_key),
    ]
)

# run the pipeline
nodes = pipeline.run(documents = loaded_docs)

for node in nodes:
    print(node)