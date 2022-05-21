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
            count = counter.count()
            alphabet = counter.get_alphabet()
            prob = 0
            for letter in alphabet:
                prob += count[letter] * (count[letter] - 1)
            length = 0
            for character in self.text:
                if counter.is_lower():
                    character = character.lower()
                if character in alphabet:
                    length += 1
            self.ic = prob / (length * (length - 1))
        return self.ic
