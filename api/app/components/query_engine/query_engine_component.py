from app.settings.settings import Settings
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import VectorStoreIndex, get_response_synthesizer

from llama_index.core.retrievers import VectorIndexRetriever




class QueryEngineComponent:
    query_engine:RetrieverQueryEngine

    def __init__(self,index:VectorStoreIndex,settings:Settings):
        self.settings = settings
        self.index = index
        self.query_engine = RetrieverQueryEngine(
            retriever=VectorIndexRetriever(
                index = index,
                similarity_top_k = settings.retriever.similarity_top_k,
                ),
            response_synthesizer=get_response_synthesizer(
                    response_mode=settings.response.response_mode,
                ),
            node_postprocessors=settings.nodepostproc.post_processors
            )