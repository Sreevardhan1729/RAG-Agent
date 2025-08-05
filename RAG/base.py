import logging, os
from langchain_core.tools import tool
from indexer import SimpleIndexer
from langgraph.prebuilt import ToolNode,tools_condition
from langgraph.graph import END,StateGraph
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv,find_dotenv
from typing import Dict,List
load_dotenv(find_dotenv())

logger = logging.getLogger(__name__)
@tool(response_format="content_and_artifact")
def retrieve(query: str,indexer: SimpleIndexer):
    """Retrieve information related to a query."""
    return indexer.query(query=query)

class RAG:
    def __init__(self,indexer: SimpleIndexer):
        logging.info("Loading the LLM")
        if not os.environ.get("GOOGLE_API_KEY"):
            raise FileNotFoundError
        logger.info("Getting the model")
        self.llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
        logging.info("Initialing the Graph")
        self.indexer = indexer
    