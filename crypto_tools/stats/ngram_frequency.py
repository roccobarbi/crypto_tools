from .ngram_counter import NgramCounter


class NgramFrequency:
    def __init__(self, nvalue=2, text="", joined=True):
        self.text = text
        self.nvalue = int(nvalue)
        self.joined = joined
        self.frequency = {}
        self.ngram_count = NgramCounter(nvalue=nvalue, text=text, joined=joined)

    def __repr__(self):
        return 'NgramFrequency(nvalue={nvalue}, text={text}, joined={joined})'.format(
            nvalue=self.nvalue,
            text=self.text,
            joined=self.joined
        )

    def __str__(self):
        frequency = self.calculate()
        return '{}'.format({", ".join(": ".join([str(c), str(frequency[c])]) for c in frequency)})

    def calculate(self):
        if self.frequency == {} and len(self.text.strip()) > 0:
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
