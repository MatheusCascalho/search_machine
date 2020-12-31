from typing import List, Dict
from models.ranking import Ranking
from models.document import Document
import os

class SearchMachine:
    def __init__(self,
                 directory: str):
        self.directory: str = directory
        self.documents: List[Document] = [Document(f'{directory}/{file}') for file in os.listdir(directory)]
        self.inverted_index = self.get_inverted_index()

    def search(self,
               expresion_search: str) -> Ranking:
        pass

    def get_inverted_index(self) -> Dict[str, List[Document]]:
        pass

    def similarity(self):
        pass

    def idf(self, word):
        pass