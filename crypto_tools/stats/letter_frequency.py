from .letter_counter import LetterCounter


class LetterFrequency:
    def __init__(self, text=""):
        self.text = text
        self.frequency = {}
        self.letter_count = LetterCounter(text=text)

    def __repr__(self):
        return 'LetterFrequency(text=%s)' % self.text

    def __str__(self):
        frequency = self.calculate()
        return '[%s]' % ({", ".join(": ".join([str(c), str(frequency[c])]) for c in frequency)})

    def calculate(self):
        if len(self.text.strip()) == 0:
            return {}
        if self.frequency == {}:
            counter = self.letter_count.count()
            length = 0
            for item in counter.keys():
                length += counter[item]
            for item in counter.keys():
                self.frequency[item] = counter[item] / length
        return self.frequency

    def set_text(self, text):
        self.text = text
        self.frequency = {}
        self.letter_count = LetterCounter(text=text)

    def get_text(self):
        return self.text

    def get_alphabet(self):
        return self.letter_count.get_alphabet()