import unittest
from UkrTranslit.Kmu2010 import Kmu2010


class Test_Kmu2010(unittest.TestCase):
    def setUp(self) -> None:
        self.trans = Kmu2010()

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


if __name__ == '__main__':
    unittest.main()