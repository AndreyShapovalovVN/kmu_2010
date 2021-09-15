import unittest
from Kmu2010.translit import Kmu2010, Cyrl2Latn


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.trans = Kmu2010()
        self.c2l = Cyrl2Latn('Kmu2010')

    def test_0(self):
        self.assertEquals(self.trans.translateral(None, 'Б'), 'B')
        self.assertEquals(self.trans.translateral(None, 'б'), 'b')

    def test_1(self):
        self.assertEquals(self.trans.translateral(None, 'Є'), 'YE')

    def test_2(self):
        self.assertEquals(self.trans.translateral('п', 'Є'), 'IE')

    def test_3(self):
        self.assertEquals(self.trans.translateral('З', 'Г'), 'GH')

    def test_4(self):
        self.assertEquals(self.trans.translateral('В', 'Г'), 'H')

    def test_5(self):
        self.assertEquals(self.c2l.cyrl_text('Андрій Петров').latn_text, 'Andrii Petrov')

    def test_6(self):
        self.assertEquals(self.c2l.cyrl_text('Дар\'я Петрова').latn_text, 'Daria Petrova')

    def test_7(self):
        self.assertEquals(self.c2l.cyrl_text('Андрій Шаповалов').latn_text, 'Andrii Shapovalov')


if __name__ == '__main__':
    unittest.main()