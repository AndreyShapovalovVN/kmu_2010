from UkrTranslit import tabl


class Cyrl2Latn:
    def __init__(self, method):
        self.trans = tabl[method]()
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
