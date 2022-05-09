from ..utils import string_utils


class NgramCounter:
    def __init__(self, nvalue=2, text="", joined=True, alphabet="abcdefghijklmnopqrstuvwxyz", lower=True):
        if lower:
            self.text = text.lower()
        else:
            self.text = text
        self.nvalue = int(nvalue)
        self.joined = joined
        self.counter = {}
        self.alphabet = alphabet
        self.lower = lower

    def __repr__(self):
        return 'NgramCounter(nvalue={nvalue}, text={text}, joined={joined}, alphabet={alphabet}, lower={lower})'.format(
            nvalue=self.nvalue,
            text=self.text,
            joined=self.joined,
            alphabet=self.alphabet,
            lower=self.lower
        )

    def __str__(self):
        counter = self.count()
        return '{}'.format({", ".join(": ".join([str(c), str(counter[c])]) for c in counter)})

    def count(self):
        if self.counter == {}:
            if self.joined:
                text = "".join(self.text.split())
            else:
                text = self.text
            for position, character in enumerate(text[:-self.nvalue + 1]):
                if self.counter == {}:
                    print(text[position:position + self.nvalue])
                if not string_utils.has_whitespace(text[position:position + self.nvalue]):
                    if not string_utils.includes_other_letters(text[position:position + self.nvalue], self.alphabet):
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
