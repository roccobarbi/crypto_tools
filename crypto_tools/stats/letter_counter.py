class LetterCounter:
    def __init__(self, text="", alphabet='abcdefghijklmnopqrstuvwxyz'):
        self.text = text
        self.alphabet = alphabet
        self.counter = {}
        self.lower = True
        for character in self.alphabet:
            if character.isupper():
                self.lower = False

    def __repr__(self):
        return 'LetterCounter(text=%s, alphabet=[%s])' % (self.text, {", ".join(str(c) for c in self.alphabet)})

    def __str__(self):
        counter = self.count()
        return '[%s]' % ({", ".join(": ".join([str(c), str(counter[c])]) for c in counter)})

    def count(self):
        """
        If the alphabet only includes lowercase letters, convert the text to lowercase before the count.
        """
        if self.counter == {}:
            if self.lower:
                for letter in self.alphabet:
                    self.counter[str(letter).lower()] = 0
            for character in self.text:
                if character.isalnum():
                    character = str(character).lower()
                if character in self.alphabet:
                    self.counter[character] += 1
        return self.counter

    def set_text(self, text):
        self.text = text
        self.counter = {}

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet
        self.counter = {}

    def get_text(self):
        return self.text

    def is_lower(self):
        return self.lower

    def get_alphabet(self):
        if self.alphabet == [] and len(self.text) > 0:
            for character in self.text:
                if character not in self.alphabet:
                    self.alphabet.append(character)
        return self.alphabet
