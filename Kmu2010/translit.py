from abc import ABC, abstractmethod


class TL(ABC):
    UKR = {}

    @abstractmethod
    def translateral(self, previous, letter):
        return self


class Kmu2010(TL):
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

    def translateral(self, previous, letter):
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


class Cyrl2Latn:
    def __init__(self, method):
        self.trans = Kmu2010()
        self._lat_text = []

    def cyrl_text(self, text):
        self._lat_text = []

        for word in text.split():
            for l in range(len(word)):
                if l == 0:
                    self._lat_text.append(self.trans.translateral(None, word[l]))
                    continue
                elif l == 1:
                    if len(self._lat_text[-1]) > 1:
                        if word[l].islower() != self._lat_text[-1].islower():
                            first = self._lat_text[-1][0].upper()
                            other = self._lat_text[-1][1:].lower()
                            self._lat_text[-1] = ''.join((first, other))
                    self._lat_text.append(self.trans.translateral(word[l - 1], word[l]))
                    continue
                else:
                    self._lat_text.append(self.trans.translateral(word[l - 1], word[l]))
                    continue

            self._lat_text.append(' ')
        return self

    @property
    def latn_text(self):
        return ''.join(self._lat_text).strip()
