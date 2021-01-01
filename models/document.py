from typing import List, Dict
from functools import total_ordering
from abc import ABCMeta


class Information:
    def __init__(self,
                 name: str,
                 content: str = ""):
        self.name = name
        self.__content = content
        self.term_frequencies = term_frequency(self.content)
        self.coordinates = None

    @property
    def content(self):
        return self.__content

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    @total_ordering
    def __lt__(self, other):
        return self.name < other.name


class Document(Information):
    def __init__(self,
                 filepath: str):
        super().__init__(name=filepath)
        self.filepath = filepath

    def content(self) -> str:
        """
        Print file text
        """
        text = ""
        with open(self.filepath, 'r') as file:
            for line in file:
                text += line
        return text


class Query(Information):
    def __init__(self, query: str):
        super().__init__(name='QUERY', content=query)

def term_frequency(text: str) -> Dict[str, int]:
    words = text.split()
    words = [word.lower().strip(".,!?") for word in words]
    tf = {}
    for word in words:
        if word not in tf:
            tf[word] = 1
        else:
            tf[word] += 1
    return tf


def get_name(filepath):
    while '/' in filepath:
        idx = filepath.index('/')
        filepath = filepath[idx + 1:]
    return filepath
