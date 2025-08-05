from loaders.base import DocumentLoader
from loaders.TextLoader import RawTextLoader
from typing import List
from langchain_core.documents import Document

def pickLoader(kind: str) -> List[Document]:
    if kind=="text":
        return RawTextLoader()
    raise NotImplementedError
__all__ = [
    "DocumentLoader",
    "TextLoader"
]