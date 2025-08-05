from loaders import DocumentLoader
from langchain_core.documents import Document
from typing import List



class RawTextLoader(DocumentLoader):
    def load(self, text:str) -> List[Document]:
        return [Document(page_content=text,metadata={"source":"user_input"})]