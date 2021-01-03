from typing import List, Dict
from models.document import Document, Query, Information
import os
import pandas as pd
import math

class SearchMachine:
    def __init__(self,
                 directory: str):
        """
        Search Machine Object. This class is created from an directory (documents space of search) and implement methods
        to search a document from query
        Args:
            directory: directory of documents (space of search)
        """
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
        self.calc_documents_coordinates()

    def calc_documents_coordinates(self):
        """
        Calculate coordinates for each document in space search.
        Returns:

        """
        for document in self.documents:
            self.calc_coordinates(document)

    def calc_coordinates(self, information: Information) -> None:
        """
        Calculate coordinates from an information object and set it on information.coordinate attribute.
        A Coordinate is an vector (pandas.Series) where each dimension (position) is a word from search machine
        vocabulary and its value is calculated as:
            word coordinate = term_frequecy in information (tf) * inverted documents frequecy (idf)
        Args:
            information [Information]:

        Returns:

        """
        coordinates = {}
        for word in self.vocabulary:
            tf = information.term_frequencies.get(word, 0)
            idf = self.idf(word)
            coordinate = tf * idf
            coordinates[word] = coordinate
        coordinates = pd.Series(coordinates)
        information.coordinates = coordinates

    def get_inverted_index(self) -> pd.DataFrame:
        """
        Get inverted index of seach space.
        An inverted index is a table (pandas.Dataframe) where each row is an word of search machine vocabulary and each
        column is an document. Each cell of inverted index can be filled by 1 (if this word occurs in this document)

        E.g.:
            d1.txt = "Hello"
            d2.txt = "Hello World"
            inverted index =
                        d1.txt  | d2.txt|
                hello  |   1    |   0   |
                world  |   1    |   1   |

        Returns:
            inverted index [pandas.DataFrame]

        """
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


    def idf(self, word: str) -> float:
        """
        inverse of word frequency in documents (idf).
        Is calculated as:
            idf = log(n/nt)
        where n is total documents in search space and nt is the number of documents where word occurs
        Args:
            word:

        Returns:
            idf
        """
        n = len(self.documents)
        where_occurs = [doc for doc in self.documents if word in doc.term_frequencies.keys()]
        nt = len(where_occurs)
        idf = math.log2(n / nt)
        return idf

    def similarity(self, document: Document, query: Query) -> float:
        """
        Similarity between document and query, calculated by cosine of coordinates attribute
        This calculus is described in ../docs/TP_PDS2-maquina_de_busca.pdf, page 4.

        Args:
            document:
            query:

        Returns:

        """
        numerator = 0
        denominator_from_query = 0
        denominator_from_document = 0
        for word in self.vocabulary:
            if word not in query.content:
                continue
            weight_in_document = document.coordinates.get(word, 0)
            weight_in_query = query.coordinates.get(word, 0)

            numerator += weight_in_document * weight_in_query
            denominator_from_document += weight_in_document**2
            denominator_from_query += weight_in_query**2
        denominator = (math.sqrt(denominator_from_document) * math.sqrt(denominator_from_query))
        if denominator == 0:
            denominator = 1
        sim = numerator / denominator
        return sim

    def search(self,
               expresion_search: str) -> list:
        """
        Search and rank documents in space search by cosine similarity
        Args:
            expresion_search [str]

        Returns:
            ranking of documents [list]
        """
        query = Query(expresion_search)
        self.calc_coordinates(query)
        similarities = {doc.label: self.similarity(document=doc, query=query) for doc in self.documents}
        ranking = [doc for doc in sorted(similarities, key=similarities.get, reverse=True)]
        return ranking
