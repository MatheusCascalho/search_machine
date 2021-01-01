from typing import List, Dict
from models.ranking import Ranking
from models.document import Document
import os
import pandas as pd
import math

class SearchMachine:
    def __init__(self,
                 directory: str):
        self.directory: str = directory
        self.documents: List[Document] = [Document(f'{directory}/{file}') for file in os.listdir(directory)]
        self.documents.sort()
        vocabulary = {word
                      for doc in self.documents
                      for word in doc.term_frequencies.keys()}
        vocabulary = list(vocabulary)
        vocabulary.sort()
        self.vocabulary = vocabulary
        self.inverted_index = self.get_inverted_index()
        self.calc_coordinates()

    def calc_coordinates(self):
        for doc in self.documents:
            coordinates = {}
            for word in self.vocabulary:
                tf = doc.term_frequencies.get(word, 0)
                idf = self.idf(word)
                coordinate = tf * idf
                coordinates[word] = coordinate
            coordinates = pd.Series(coordinates, )
            doc.coordinates = coordinates


    def search(self,
               expresion_search: str) -> Ranking:
        pass

    def get_inverted_index(self) -> Dict[str, List[Document]]:
        index = {}
        columns = []
        for word in self.vocabulary:
            index[word] = []
            for document in self.documents:
                if len(columns) < len(self.documents):
                    columns.append(str(document))
                value = 1 if word in document.term_frequencies.keys() else 0
                index[word].append(value)
        df = pd.DataFrame(index).transpose()
        df.columns = columns
        return df

    def similarity(self):
        pass

    def idf(self, word):
        n = len(self.documents)
        where_occurs  = [doc for doc in self.documents if word in doc.term_frequencies.keys()]
        nt = len(where_occurs)
        idf = math.log2(n / nt)
        return idf