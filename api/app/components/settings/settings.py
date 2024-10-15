from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import SentenceSplitter
import tiktoken
from llama_index.core.extractors import TitleExtractor
from llama_index.core import Settings

Settings.embed_model = OpenAIEmbedding(
    model= "text-embedding-3-large",
    dimensions=1024)

Settings.llm = OpenAI(
    model = "gpt-3.5-turbo",
    temperature = 0.1,
)

Settings.tokenizer = tiktoken.encoding_for_model(
    "gpt-3.5-turbo").encode

Settings.transformations = [
    SentenceSplitter(chunk_size=1024, chunk_overlap=50),
    TitleExtractor(),
    Settings.embed_model,
    ]


