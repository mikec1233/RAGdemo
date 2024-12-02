#from llama_index.core.chat_engine import CondenseQuestionChatEngine
from llama_index.core.chat_engine.condense_plus_context import CondensePlusContextChatEngine 
#from llama_index.core.chat_engine.types import ReActChatEngine
from llama_index.core.tools import QueryEngineTool
from llama_index.core.memory import ChatMemoryBuffer
from app.settings.settings import Settings
from app.components.query_engine.query_engine_component import QueryEngineComponent
from app.components.llm.llm_component import LLMComponent

class ChatEngineComponent:
    def __init__(self, query_engine_component: QueryEngineComponent, settings: Settings):
        self.settings = settings
        self.query_engine_component = query_engine_component
        self.llm_component = LLMComponent(settings)
        
        self.memory = ChatMemoryBuffer.from_defaults(token_limit=1500)

        #adding QueryEngineTool, essentially a wrapper around the query engine so that it may be called in ReAct Engine.
        # self.query_engine_tool = QueryEngineTool.from_defaults(
        #     query_engine=query_engine_component.query_engine,
        #     description="Useful for answering questions about R packages and their validation details."
        # )

        # Initialize the ReActChatEngine
        # self.chat_engine = ReActChatEngine.from_defaults(
        #     llm=self.llm_component.llm,
        #     tools=[self.query_engine_tool],
        #     memory=self.memory,
        #     verbose=True
        # )

        # self.chat_engine = CondenseQuestionChatEngine.from_defaults(
        #     llm=self.llm_component.llm,
        #     query_engine=self.query_engine_component.query_engine,
        #     memory=self.memory,
        #     verbose=True,
        #     system_prompt_template=self.llm_component.PROMPT_TEMPLATE,
        #     chat_mode='condense_plus_context'
        # )

        self.chat_engine = CondensePlusContextChatEngine.from_defaults(
            retriever=self.query_engine_component.retriever,
            llm=self.llm_component.llm,
            query_engine=self.query_engine_component.query_engine,
            memory=self.memory,
            verbose=True,
            system_prompt_template=self.llm_component.PROMPT_TEMPLATE,
            chat_mode='condense_plus_context'
        )


    def chat(self, message: str) -> str:
        response = self.chat_engine.chat(message)
        return str(response)
    