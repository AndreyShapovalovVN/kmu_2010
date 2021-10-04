import unittest
from UkrTranslit.translit import Cyrl2Latn


class Test_c2l(unittest.TestCase):
    def setUp(self) -> None:
        self.c2l = Cyrl2Latn('Kmu2010')

    def test_0(self):
        self.assertEquals(self.c2l.cyrl_text('Андрій Петров').latn_text, 'Andrii Petrov')

    def test_1(self):
        self.assertEquals(self.c2l.cyrl_text('Дар\'я Петрова').latn_text, 'Daria Petrova')

    def test_2(self):
        self.assertEquals(self.c2l.cyrl_text('Андрій Шаповалов').latn_text, 'Andrii Shapovalov')

    def test_3(self):
        self.assertEquals(self.c2l.cyrl_text('Андрій ШАПОВАЛОВ').latn_text, 'Andrii SHAPOVALOV')

    def test_4(self):
        self.assertEquals(self.c2l.cyrl_text('Андрій шаповалов').latn_text, 'Andrii shapovalov')


if __name__ == '__main__':
    unittest.main()