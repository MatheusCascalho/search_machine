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
        tf = term_frequency('../files/d1.txt')
        self.assertDictEqual(expected, tf)

    def test_get_name(self):
        expected = "d1.txt"
        name = get_name('../files/d1.txt')
        self.assertEqual(expected, name)

    def test_text(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        expected = "Ola, meu nome é matheus\nQual é o seu?\n"
        Document('../files/d1.txt').text()
        text = capturedOutput.getvalue()
        self.assertEqual(expected, text)



if __name__ == '__main__':
    unittest.main()
