import unittest
import unittest.mock
from models.document import Document, term_frequency, get_name
import io
import sys
import pytest

class MyTestCase(unittest.TestCase):
    def test_term_frequency(self):
        expected = {
            "ola": 1,
            "meu": 1,
            "nome": 1,
            "é": 2,
            "matheus": 1,
            "qual": 1,
            "o": 1,
            "seu": 1
        }
        input = "Ola, meu nome é matheus.\nQual é o seu?"
        tf = term_frequency(input)
        self.assertDictEqual(expected, tf)

    def test_get_name(self):
        expected = "d1.txt"
        name = get_name('../test_files/d1.txt')
        self.assertEqual(expected, name)



if __name__ == '__main__':
    unittest.main()
