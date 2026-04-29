"""
Тести транслітерації за правилами КМУ 2010.
Постанова КМУ від 27.01.2010 № 55.
"""

import unittest
from UkrTranslit.Kmu2010 import Kmu2010


class TestTranslateral(unittest.TestCase):
    """Тести методу translateral() — транслітерація однієї літери."""

    def setUp(self) -> None:
        self.t = Kmu2010()

    # ------------------------------------------------------------------
    # Регістр
    # ------------------------------------------------------------------
    def test_uppercase_letter(self):
        self.assertEqual(self.t.translateral(None, 'Б'), 'B')

    def test_lowercase_letter(self):
        self.assertEqual(self.t.translateral(None, 'б'), 'b')

    def test_multichar_uppercase(self):
        """Багатосимвольний результат (ШЧ) — весь у верхньому регістрі."""
        self.assertEqual(self.t.translateral(None, 'Щ'), 'SHCH')

    def test_multichar_lowercase(self):
        """Багатосимвольний результат (шч) — весь у нижньому регістрі."""
        self.assertEqual(self.t.translateral(None, 'щ'), 'shch')

    # ------------------------------------------------------------------
    # Усі літери алфавіту — основна форма (після іншої літери)
    # ------------------------------------------------------------------
    def test_А(self): self.assertEqual(self.t.translateral('б', 'А'), 'A')
    def test_Б(self): self.assertEqual(self.t.translateral('б', 'Б'), 'B')
    def test_В(self): self.assertEqual(self.t.translateral('б', 'В'), 'V')
    def test_Г(self): self.assertEqual(self.t.translateral('б', 'Г'), 'H')
    def test_Ґ(self): self.assertEqual(self.t.translateral('б', 'Ґ'), 'G')
    def test_Д(self): self.assertEqual(self.t.translateral('б', 'Д'), 'D')
    def test_Е(self): self.assertEqual(self.t.translateral('б', 'Е'), 'E')
    def test_Є_mid(self): self.assertEqual(self.t.translateral('п', 'Є'), 'IE')
    def test_Ж(self): self.assertEqual(self.t.translateral('б', 'Ж'), 'ZH')
    def test_З(self): self.assertEqual(self.t.translateral('б', 'З'), 'Z')
    def test_И(self): self.assertEqual(self.t.translateral('б', 'И'), 'Y')
    def test_І(self): self.assertEqual(self.t.translateral('б', 'І'), 'I')
    def test_Ї_mid(self): self.assertEqual(self.t.translateral('а', 'Ї'), 'I')
    def test_Й_mid(self): self.assertEqual(self.t.translateral('а', 'Й'), 'I')
    def test_К(self): self.assertEqual(self.t.translateral('б', 'К'), 'K')
    def test_Л(self): self.assertEqual(self.t.translateral('б', 'Л'), 'L')
    def test_М(self): self.assertEqual(self.t.translateral('б', 'М'), 'M')
    def test_Н(self): self.assertEqual(self.t.translateral('б', 'Н'), 'N')
    def test_О(self): self.assertEqual(self.t.translateral('б', 'О'), 'O')
    def test_П(self): self.assertEqual(self.t.translateral('б', 'П'), 'P')
    def test_Р(self): self.assertEqual(self.t.translateral('б', 'Р'), 'R')
    def test_С(self): self.assertEqual(self.t.translateral('б', 'С'), 'S')
    def test_Т(self): self.assertEqual(self.t.translateral('б', 'Т'), 'T')
    def test_У(self): self.assertEqual(self.t.translateral('б', 'У'), 'U')
    def test_Ф(self): self.assertEqual(self.t.translateral('б', 'Ф'), 'F')
    def test_Х(self): self.assertEqual(self.t.translateral('б', 'Х'), 'KH')
    def test_Ц(self): self.assertEqual(self.t.translateral('б', 'Ц'), 'TS')
    def test_Ч(self): self.assertEqual(self.t.translateral('б', 'Ч'), 'CH')
    def test_Ш(self): self.assertEqual(self.t.translateral('б', 'Ш'), 'SH')
    def test_Щ(self): self.assertEqual(self.t.translateral('б', 'Щ'), 'SHCH')
    def test_Ь(self): self.assertEqual(self.t.translateral('б', 'Ь'), '')
    def test_Ю_mid(self): self.assertEqual(self.t.translateral('к', 'Ю'), 'IU')
    def test_Я_mid(self): self.assertEqual(self.t.translateral('н', 'Я'), 'IA')

    # ------------------------------------------------------------------
    # Літери, що мають альтернативну форму на початку слова
    # ------------------------------------------------------------------
    def test_Є_start(self):
        """Є на початку слова → YE."""
        self.assertEqual(self.t.translateral(None, 'Є'), 'YE')

    def test_є_start(self):
        """є на початку слова → ye."""
        self.assertEqual(self.t.translateral(None, 'є'), 'ye')

    def test_Ї_start(self):
        """Ї на початку слова → YI."""
        self.assertEqual(self.t.translateral(None, 'Ї'), 'YI')

    def test_ї_start(self):
        """ї на початку слова → yi."""
        self.assertEqual(self.t.translateral(None, 'ї'), 'yi')

    def test_Й_start(self):
        """Й на початку слова → Y."""
        self.assertEqual(self.t.translateral(None, 'Й'), 'Y')

    def test_й_start(self):
        """й на початку слова → y."""
        self.assertEqual(self.t.translateral(None, 'й'), 'y')

    def test_Ю_start(self):
        """Ю на початку слова → YU."""
        self.assertEqual(self.t.translateral(None, 'Ю'), 'YU')

    def test_ю_start(self):
        """ю на початку слова → yu."""
        self.assertEqual(self.t.translateral(None, 'ю'), 'yu')

    def test_Я_start(self):
        """Я на початку слова → YA."""
        self.assertEqual(self.t.translateral(None, 'Я'), 'YA')

    def test_я_start(self):
        """я на початку слова → ya."""
        self.assertEqual(self.t.translateral(None, 'я'), 'ya')

    # ------------------------------------------------------------------
    # Спеціальне правило «зг» → «zgh»
    # ------------------------------------------------------------------
    def test_ЗГ_uppercase(self):
        """Г після З (обидва великі) → GH."""
        self.assertEqual(self.t.translateral('З', 'Г'), 'GH')

    def test_зг_lowercase(self):
        """г після з (обидва малі) → gh."""
        self.assertEqual(self.t.translateral('з', 'г'), 'gh')

    def test_Зг_mixed(self):
        """г після З (мала г) → gh."""
        self.assertEqual(self.t.translateral('З', 'г'), 'gh')

    def test_Г_not_after_З(self):
        """Г після іншої літери (не З) → H."""
        self.assertEqual(self.t.translateral('В', 'Г'), 'H')

    def test_Г_start(self):
        """Г на початку слова → H."""
        self.assertEqual(self.t.translateral(None, 'Г'), 'H')

    # ------------------------------------------------------------------
    # М'який знак
    # ------------------------------------------------------------------
    def test_Ь_upper(self):
        """Ь не передається латиницею → порожній рядок."""
        self.assertEqual(self.t.translateral(None, 'Ь'), '')

    def test_ь_lower(self):
        """ь не передається латиницею → порожній рядок."""
        self.assertEqual(self.t.translateral(None, 'ь'), '')


class TestTransliterate(unittest.TestCase):
    """
    Тести методу transliterate() — транслітерація рядка.

    Приклади взяті з таблиці 2 Постанови КМУ № 55 від 27.01.2010.
    """

    def setUp(self) -> None:
        self.t = Kmu2010()

    # ------------------------------------------------------------------
    # Приклади з офіційної таблиці регламенту KMU 2010
    # ------------------------------------------------------------------
    def test_alushta(self):
        self.assertEqual(self.t.transliterate('алушта'), 'alushta')

    def test_borshchahivka(self):
        self.assertEqual(self.t.transliterate('борщагівка'), 'borshchahivka')

    def test_vinnytsia(self):
        """вінниця — подвійне н, ц, я після приголосної → ia."""
        self.assertEqual(self.t.transliterate('вінниця'), 'vinnytsia')

    def test_dnipro(self):
        self.assertEqual(self.t.transliterate('дніпро'), 'dnipro')

    def test_yenakiieve(self):
        """Є на початку → ye; є після приголосної → ie."""
        self.assertEqual(self.t.transliterate('єнакієве'), 'yenakiieve')

    def test_yizhakevych(self):
        """Ї на початку → yi."""
        self.assertEqual(self.t.transliterate('їжакевич'), 'yizhakevych')

    def test_zolotonosha(self):
        self.assertEqual(self.t.transliterate('золотоноша'), 'zolotonosha')

    def test_kovel_soft_sign(self):
        """М'який знак (ь) не передається."""
        self.assertEqual(self.t.transliterate('ковель'), 'kovel')

    def test_mykolaiv(self):
        """Ї після голосної → i (Миколаїв → Mykolaiv)."""
        self.assertEqual(self.t.transliterate('миколаїв'), 'mykolaiv')

    def test_odesa(self):
        self.assertEqual(self.t.transliterate('одеса'), 'odesa')

    def test_poltava(self):
        self.assertEqual(self.t.transliterate('полтава'), 'poltava')

    def test_romny(self):
        self.assertEqual(self.t.transliterate('ромни'), 'romny')

    def test_sumy(self):
        self.assertEqual(self.t.transliterate('суми'), 'sumy')

    def test_ternopil_soft_sign(self):
        """Ль — м'який знак не передається."""
        self.assertEqual(self.t.transliterate('тернопіль'), 'ternopil')

    def test_kharkiv(self):
        self.assertEqual(self.t.transliterate('харків'), 'kharkiv')

    def test_kherson(self):
        self.assertEqual(self.t.transliterate('херсон'), 'kherson')

    def test_khmelnytskyi(self):
        """Складне слово з кількома м'якими знаками та Й після И."""
        self.assertEqual(self.t.transliterate('хмельницький'), 'khmelnytskyi')

    def test_cherkasy(self):
        self.assertEqual(self.t.transliterate('черкаси'), 'cherkasy')

    def test_chernihiv(self):
        self.assertEqual(self.t.transliterate('чернігів'), 'chernihiv')

    def test_shostka(self):
        self.assertEqual(self.t.transliterate('шостка'), 'shostka')

    def test_shcherbukhy(self):
        self.assertEqual(self.t.transliterate('щербухи'), 'shcherbukhy')

    def test_yurii(self):
        """Ю на початку → yu; Й після голосної → i."""
        self.assertEqual(self.t.transliterate('юрій'), 'yurii')

    def test_yahotyn(self):
        """Я на початку → ya."""
        self.assertEqual(self.t.transliterate('яготин'), 'yahotyn')

    def test_zghurskyi(self):
        """Сполучення зг → zgh."""
        self.assertEqual(self.t.transliterate('згурський'), 'zghurskyi')

    def test_kyiv(self):
        """Київ: ї після и → i."""
        self.assertEqual(self.t.transliterate('київ'), 'kyiv')

    # ------------------------------------------------------------------
    # Регістр
    # ------------------------------------------------------------------
    def test_uppercase_word(self):
        """Весь рядок у верхньому регістрі."""
        self.assertEqual(self.t.transliterate('ХАРКІВ'), 'KHARKIV')

    def test_uppercase_shch(self):
        """Щ у верхньому регістрі → SHCH."""
        self.assertEqual(self.t.transliterate('ЩЕРБУХИ'), 'SHCHERBUKHY')

    # ------------------------------------------------------------------
    # Змішаний вміст та речення
    # ------------------------------------------------------------------
    def test_non_ukrainian_passthrough(self):
        """Не-українські символи залишаються без змін."""
        self.assertEqual(self.t.transliterate('Kyiv 2024'), 'Kyiv 2024')

    def test_sentence(self):
        """Речення з кількома словами."""
        self.assertEqual(self.t.transliterate('місто київ'), 'misto kyiv')

    def test_word_boundary_resets_context(self):
        """Пробіл між словами скидає контекст: Є на початку слова → ye."""
        self.assertEqual(self.t.transliterate('де єнакієве'), 'de yenakiieve')

    def test_hyphen_resets_context(self):
        """Дефіс скидає контекст: Є після дефісу → ye."""
        self.assertEqual(self.t.transliterate('де-єнакієве'), 'de-yenakiieve')

    def test_digits_preserved(self):
        """Цифри зберігаються."""
        self.assertEqual(self.t.transliterate('вулиця 123'), 'vulytsia 123')

    def test_empty_string(self):
        self.assertEqual(self.t.transliterate(''), '')

    def test_no_ukrainian(self):
        """Рядок без українських літер повертається без змін."""
        self.assertEqual(self.t.transliterate('Hello, World!'), 'Hello, World!')


if __name__ == '__main__':
    unittest.main()

