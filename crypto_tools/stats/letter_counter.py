class LetterCounter:
    def __init__(self, text="", alphabet=[]):
        self.text = text
        self.alphabet = alphabet
        self.counter = {}

    def __repr__(self):
        return 'LetterCounter(text=%s, alphabet=[%s])' % (self.text, {", ".join(str(c) for c in self.alphabet)})

    def __str__(self):
        counter = self.count()
        return '[%s]' % ({", ".join(": ".join([str(c), str(counter[c])]) for c in counter)})

    def count(self):
        if self.counter == {}:
            for letter in self.alphabet:
                self.counter[str(letter).lower()] = 0
            for character in self.text:
                if character.isalnum():
                    standardised_character = str(character).lower()
                    if standardised_character not in self.alphabet:
                        self.alphabet.append(standardised_character)
                        self.counter[standardised_character] = 1
                    else:
                        self.counter[standardised_character] += 1
        return self.counter

    def set_text(self, text):
        self.text = text
        self.counter = {}

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet
        self.counter = {}

    def get_text(self):
        return self.text

    def get_alphabet(self):
        if self.alphabet == [] and len(self.text) > 0:
            for character in self.text:
                if character not in self.alphabet:
                    self.alphabet.append(character)
        return self.alphabet
