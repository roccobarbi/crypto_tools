class NgramCounter:
    def __init__(self, text=""):
        self.text = text
        self.counter = {}

    def __repr__(self):
        return 'NgramCounter(text=%s)' % self.text

    def __str__(self):
        counter = self.count()
        return '[%s]' % ({", ".join(": ".join([str(c), str(counter[c])]) for c in counter)})

    def count(self):
        if self.counter == {}:
            for position, character in enumerate(self.text[:-1]):
                if character.isalnum() and self.text[position + 1].isalnum():
                    if self.text[position:position + 1] not in self.counter.keys():
                        self.counter[self.text[position:position + 1]] = 1
                    else:
                        self.counter[self.text[position:position + 1]] += 1
        return self.counter

    def set_text(self, text):
        self.text = text
        self.counter = {}

    def get_text(self):
        return self.text
