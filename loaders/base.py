from langchain_core.documents import Document
from typing import List
class DocumentLoader:
    """Base class with one public method. """
    def load(self,source:str) -> List[Document]:
        raise NotImplementedError
    