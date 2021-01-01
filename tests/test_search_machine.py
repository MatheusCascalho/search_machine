import unittest
from models.search_machine import SearchMachine
import pandas as pd

class MyTestCase(unittest.TestCase):
    def test_get_inverted_index(self):
        sm = SearchMachine('../files')
        index = sm.get_inverted_index()
        data = {
            "felipe": [0, 0, 1],
            "marcos": [0, 1, 1],
            "matheus": [1, 0, 0],
            "meu": [1, 0, 0],
            "nome": [1, 0, 0],
            "o": [1, 0, 0],
            "ola": [1, 0, 0],
            "qual": [1, 0, 0],
            "seu": [1, 0, 0],
            "é": [1, 0, 0],
        }
        columns = ["d1.txt", "d2.txt", "d3.txt"]
        df = pd.DataFrame(data).transpose()
        df.columns = columns
        pd.testing.assert_frame_equal(df, index)


if __name__ == '__main__':
    unittest.main()
