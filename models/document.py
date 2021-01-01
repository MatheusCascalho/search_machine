from typing import List, Dict
from functools import total_ordering

class Document:
    def __init__(self,
                 filepath: str):
        self.filepath = filepath
        self.filename = get_name(filepath)
        self.term_frequencies: Dict[str, int] = term_frequency(filepath)
        self.coordinates = None

    def __repr__(self):
        return self.filepath

    def __str__(self):
        return self.filename

    def __eq__(self, other):
        return self.filename == other.filename

    @total_ordering
    def __lt__(self, other):
        return self.filename < other.filename

    def text(self) -> None:
        """
        Print file text
        """
        text = ""
        with open(self.filepath, 'r') as file:
            for line in file:
                text += line
        print(text)



def term_frequency(filepath: str) -> Dict[str, int]:
    with open(filepath, 'r') as file:
        lines = []
        for line in file:
            lines.append(line)
    words = " ".join(lines)
    words = words.split()
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
        filepath = filepath[idx+1:]
    return filepath