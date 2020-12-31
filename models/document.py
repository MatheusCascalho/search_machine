from typing import List, Dict


class Document:
    def __init__(self,
                 filepath: str):
        self.filepath = filepath
        self.term_frequencies: Dict[str, int] = term_frequency(filepath)
        self.coordinates = None

    def __repr__(self):
        return self.filepath

    def text(self) -> None:
        """
        Print file text
        """
        pass


def term_frequency(filepath: str) -> Dict[str, int]:
    file = open(filepath, 'r')
    lines = []
    for line in file:
        lines.append(line)

