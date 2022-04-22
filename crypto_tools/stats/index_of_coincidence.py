from .letter_counter import LetterCounter


class IndexOfCoincidence:

    def __init__(self, text):
        if len(text) < 2:
            raise ValueError("text shorter than 2 characters, the incidence of coincidence can't be calculated")
        self.text = text
        self.ic = None

    def calculate(self):
        if self.ic is None:
            counter = LetterCounter(text=self.text)
            alphabet = counter.count()
            ic = 0
            for letter in alphabet:
                ic += alphabet[letter] / len(self.text) * (alphabet[letter] - 1) / (len(self.text) - 1)
            self.ic = ic
        return self.ic
