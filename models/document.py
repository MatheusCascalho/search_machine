from typing import Dict
from functools import total_ordering


class Information:
    """

    """

    def __init__(self,
                 label: str,
                 content: str = ""):
        """
        Super class that model information. Each instance of information have an label and content.
        Args:
            label [str] : label of information
            content [str] : content of information

        Class Attributes:
            label
            content
            term_frequencies [dict]: frequency of each word in information
            coordinates [pandas.Series]: coordinate of document in a search space
        """
        self.label = label
        self.__content = content
        self.term_frequencies = term_frequency(self.content)
        self.coordinates = None

    @property
    def content(self):
        return self.__content

    def __repr__(self):
        return self.label

    def __str__(self):
        return self.label

    def __eq__(self, other):
        return self.label == other.label

    @total_ordering
    def __lt__(self, other):
        return self.label < other.label


class Document(Information):
    def __init__(self,
                 filepath: str):
        """
        Document class is a child class of Information. It's label attribute is the filename and content attribute is
        content of file
        Args:
            filepath [str]
        """
        name = get_name(filepath)
        self.filepath = filepath
        super().__init__(label=name)

    @property
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
        """
        Query is a child class of Information. A query (or search expression) is created by an expression (string) and
        has 'Query' as label attribute
        Args:
            query:
        """
        super().__init__(label='QUERY', content=query)


def term_frequency(text: str) -> Dict[str, int]:
    """
    Calculate frequency of each word in a text
    Args:
        text [str]

    Returns:
        term_frequency [dict]

    """
    words = text.split()
    words = [word.lower().strip(".,!?()") for word in words]
    tf = {}
    for word in words:
        if word not in tf:
            tf[word] = 1
        else:
            tf[word] += 1
    return tf


def get_name(filepath: str):
    """
    get name of file in a filepath
    Args:
        filepath [str]

    Returns:
        filename [str]
    """
    while '/' in filepath:
        idx = filepath.index('/')
        filepath = filepath[idx + 1:]
    return filepath
