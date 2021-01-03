import unittest
import unittest.mock
from models.document import Information, Query, term_frequency, get_name
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
        name = get_name('../test_files/test_document/d1.txt')
        self.assertEqual(expected, name)

    def test_content_property(self):
        info = Information(name="info_teste")
        expected = ""
        real = info.content
        self.assertEqual(real, expected)

    def test_repr_property(self):
        info = Information(name="info_teste")
        expected = "info_teste"
        real = repr(info)
        self.assertEqual(real, expected)

    def test_str_property(self):
        info = Information(name="info_teste")
        expected = "info_teste"
        real = str(info)
        self.assertEqual(real, expected)

    def test_eq_property(self):
        info1 = Information(name="info_teste")
        info2 = Information(name="info_teste")
        self.assertEqual(info1, info2)

    def test_less_property(self):
        info1 = Information(name="info_teste")
        info2 = Information(name="info_teste2")
        self.assertLess(info1, info2)

    def test_query_name(self):
        query = Query("teste")
        expected = "QUERY"
        self.assertEqual(expected, query.name)

if __name__ == '__main__':
    unittest.main()
