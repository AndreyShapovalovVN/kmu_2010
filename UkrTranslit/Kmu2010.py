class Kmu2010:
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

    def translateral(self, previous: str, letter: str) -> str:
        """
        :rtype: object
        :return: str
        :param previous: str
        :param letter: str
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
