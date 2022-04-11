class NgramCounter:
    def __init__(self, nvalue=2, text=""):
        self.text = text
        self.nvalue = int(nvalue)
        self.counter = {}

    def __repr__(self):
        return 'NgramCounter(nvalue=%s, text=%s)' % (str(self.nvalue), self.text)

    def __str__(self):
        counter = self.count()
        return '[%s]' % ({", ".join(": ".join([str(c), str(counter[c])]) for c in counter)})

    def count(self):
        if self.counter == {}:
            text = "".join(self.text.split())
            for position, character in enumerate(text[:-self.nvalue + 1]):
                if text[position:position + self.nvalue].lower() not in self.counter.keys():
                    self.counter[text[position:position + self.nvalue].lower()] = 1
                else:
                    self.counter[text[position:position + self.nvalue].lower()] += 1
        return self.counter

    def set_text(self, text):
        self.text = text
        self.counter = {}

    def get_text(self):
        return self.text
