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
