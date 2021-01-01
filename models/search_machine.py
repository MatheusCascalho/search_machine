from typing import List, Dict
from models.ranking import Ranking
from models.document import Document
import os
import pandas as pd

class SearchMachine:
    def __init__(self,
                 directory: str):
        self.directory: str = directory
        self.documents: List[Document] = [Document(f'{directory}/{file}') for file in os.listdir(directory)]
        self.documents.sort()
        self.vocabulary = {word
                           for doc in self.documents
                           for word in doc.term_frequencies.keys()}
        self.inverted_index = self.get_inverted_index()

    def search(self,
               expresion_search: str) -> Ranking:
        pass

    def get_inverted_index(self) -> Dict[str, List[Document]]:
        words = list(self.vocabulary)
        words.sort()
        index = {}
        columns = []
        for word in words:
            index[word] = []
            for document in self.documents:
                if len(columns) < len(self.documents):
                    columns.append(str(document))
                value = 1 if word in document.term_frequencies.keys() else 0
                index[word].append(value)
        # columns = [str(doc) for doc in self.documents]
        # columns.sort()
        df = pd.DataFrame(index).transpose()
        df.columns = columns
        return df

    def similarity(self):
        pass

    def idf(self, word):
        pass