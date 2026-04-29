"""
Транслітерація українського тексту латиницею (Постанова КМУ № 55, 27.01.2010).
https://zakon.rada.gov.ua/laws/show/55-2010-%D0%BF#Text
"""


class Kmu2010:
    """Транслітерація українського алфавіту латиницею за правилами КМУ 2010."""

    #: літера → (основна форма, альтернативна форма на початку слова / після «з»)
    UKR = {
        'А': ('A', None),
        'Б': ('B', None),
        'В': ('V', None),
        'Г': ('H', 'GH'),
        'Ґ': ('G', None),
        'Д': ('D', None),
        'Е': ('E', None),
        'Є': ('IE', 'YE',),
        'Ж': ('ZH', None),
        'З': ('Z', None),
        'И': ('Y', None),
        'І': ('I', None),
        'Ї': ('I', 'YI'),
        'Й': ('I', 'Y'),
        'К': ('K', None),
        'Л': ('L', None),
        'М': ('M', None),
        'Н': ('N', None),
        'О': ('O', None),
        'П': ('P', None),
        'Р': ('R', None),
        'С': ('S', None),
        'Т': ('T', None),
        'У': ('U', None),
        'Ф': ('F', None),
        'Х': ('KH', None),
        'Ц': ('TS', None),
        'Ч': ('CH', None),
        'Ш': ('SH', None),
        'Щ': ('SHCH', None),
        'Ь': ('', None),
        'Ю': ('IU', 'YU'),
        'Я': ('IA', 'YA')
    }

    def translateral(self, previous: str | None, letter: str) -> str:
        """
        Транслітерує одну літеру з урахуванням попередньої.

        :param previous: попередня літера або ``None`` якщо літера перша у слові.
        :param letter: літера для транслітерації.
        :return: латинський відповідник.
        """
        if not previous:
            if letter.upper() in 'ЄЇЙЮЯ':
                return_ = self.UKR.get(letter.upper(), (None, None))[1]
            else:
                return_ = self.UKR.get(letter.upper(), (None, None))[0]
        else:
            if previous.upper() == 'З' and letter.upper() == 'Г':
                return_ = self.UKR.get(letter.upper(), (None, None))[1]
            else:
                return_ = self.UKR.get(letter.upper(), (None, None))[0]
        if not return_:
            return ''
        return return_ if letter.isupper() else return_.lower()

    def transliterate(self, text: str) -> str:
        """
        Транслітерує рядок українського тексту латиницею.

        Не-українські символи залишаються без змін.
        Пробіл, дефіс і символи нового рядка скидають контекст початку слова.

        :param text: вхідний рядок.
        :return: транслітерований рядок.
        """
        result = []
        prev_ukr: str | None = None

        for char in text:
            upper = char.upper()
            if upper in self.UKR:
                result.append(self.translateral(prev_ukr, char))
                prev_ukr = upper
            else:
                result.append(char)
                # Пробіл, дефіс або перехід рядка — скидаємо контекст слова
                if char in ' \t\n\r-':
                    prev_ukr = None

        return ''.join(result)
