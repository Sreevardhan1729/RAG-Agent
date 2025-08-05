from loaders import pickLoader
from indexer import SimpleIndexer
from RAG import RAG
import logging
logging.basicConfig(filename="app.log",encoding="utf-8",filemode="a",format="{asctime} - {levelname} - {message}",style="{",datefmt="%Y-%m-%d %H:%M",level=logging.INFO)
with open("input.txt","r") as f:
    text = f.read()
docs = pickLoader("text").load(text)
indexer = SimpleIndexer()
indexer.add(docs)
agent = RAG(indexer)