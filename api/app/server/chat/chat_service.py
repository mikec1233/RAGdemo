from dataclasses import asdict, dataclass
from app.components.index.index_component import IndexingComponent
from app.components.client.client_component import ClientComponent
from app.components.query_engine.query_engine_component import QueryEngineComponent
from app.components.llm.llm_component import LLMComponent
from llama_index.vector_stores.opensearch import OpensearchVectorStore, OpensearchVectorClient
from llama_index.core import VectorStoreIndex
from llama_index.core.base import base_query_engine
from app.settings.settings import Settings, global_settings


class ChatService:
    def __init__(self) -> None:
        self.client=ClientComponent(global_settings).create_client()
        self.vector_store=OpensearchVectorStore(self.client)
        self.index=IndexingComponent(vector_store=self.vector_store,settings=global_settings).index
        self.query_engine=QueryEngineComponent(self.index,global_settings).query_engine
        self.llm_component = LLMComponent(global_settings)

    #this method handles the logic for generating the responsve given the users question and the relavent docs from OpenSearch.        

    def generate_response(self, context: str, question: str) -> str:
        #we get our promp declared in the llm component.
        prompt = self.llm_component.PROMPT_TEMPLATE.format(context=context, question=question)
        #we generate and return the response from the llm
        #We are using .complete right now for simple question answering. In the future we may want to switch to "chat" so that users
        #can continue to ask questions based on prior context.
        response = self.llm_component.llm.complete(prompt)
        return response.text


    def query(self, user_input: str) -> dict:
            
            
            #take user input, send to query_engine and get the result (later change to top 3 results)
            query_result = self.query_engine.query(user_input)
            print(f"Query result type: {type(query_result)}")  # Debugging
            print(f"Query result content: {query_result}")  # Debugging


            # Check for relevance threshold
            # if hasattr(query_result, "source_nodes") and query_result.source_nodes:
            #     context_text = "\n\n---\n\n".join([node.node.text for node in query_result.source_nodes])
            # else:
            #     return {"response": "No suitable results found"}
            

            context_text = query_result
            #using context_text and the initial question generate llm response
            llm_response = self.generate_response(context=context_text, question=user_input)
            print(f"LLM response type: {type(llm_response)}")  # Debugging



            return {"response": llm_response}

