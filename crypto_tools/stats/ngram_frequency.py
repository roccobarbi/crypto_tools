from .ngram_counter import NgramCounter


class NgramFrequency:
    def __init__(self, nvalue=2, text=""):
        self.text = text
        self.nvalue = int(nvalue)
        self.frequency = {}
        self.ngram_count = NgramCounter(nvalue=nvalue, text=text)

    def __repr__(self):
        return 'NgramFrequency(nvalue=%d, text=%s)' % self.nvalue, self.text

    def __str__(self):
        frequency = self.calculate()
        return '[%s]' % ({", ".join(": ".join([str(c), str(frequency[c])]) for c in frequency)})

    def calculate(self):
        if len(self.text.strip()) == 0:
            return {}
        if self.frequency == {}:
            counter = self.ngram_count.count()
            length = 0
            for item in counter.keys():
                length += counter[item]
            for item in counter.keys():
                self.frequency[item] = counter[item] / length
        return self.frequency

    def set_text(self, text):
        self.text = text
        self.frequency = {}
        self.ngram_count = NgramCounter(nvalue=self.nvalue, text=text)

    def get_text(self):
        return self.text
