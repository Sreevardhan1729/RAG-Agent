import os,logging, faiss
from dotenv import load_dotenv
import numpy as np
# from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document

from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore


load_dotenv()
logger = logging.getLogger(__name__)


class SimpleIndexer:
    def __init__(self,chunk_size:int = 500,chunk_overlap:int = 150):
        logger.info("Initializing Simple Indexer")
        logger.info("Loading embeddings model")
        self.embeddings = DeterministicFakeEmbedding(size=4096)
        logger.info("Loaded embeddings model")
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
        logger.info("Trying to access embedding dimensions")
        dim = len(self.embeddings.embed_documents(["text"])[0])
        logger.info("Loading the vector store")
        index = faiss.IndexFlatL2(dim)
        self.vector_store = FAISS(
            embedding_function=self.embeddings,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )
        logger.info("Simple Indexer Initialization Done")
    def add(self,docs: List[Document]):
        logging.info("Starting text Splitting")
        chunks = self.text_splitter.split_documents(docs)
        logging.info("Storing in vector store")
        _ = self.vector_store.add_documents(chunks)
        logging.info("Vector Storing Done")
    def query(self,query: str,k: int = 3):
        logging.info("Retrieving similar data in vector store")
        retrieved_docs = self.vector_store.similarity_search(query=query,k=k)
        logging.info("Returning the data")
        info = "\n\n".join(doc.page_content for doc in retrieved_docs)
        return info,retrieved_docs