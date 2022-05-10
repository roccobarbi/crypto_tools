import unittest
from crypto_tools.stats import letter_counter


class TestLetterCounter(unittest.TestCase):
    def test_count_empty(self):
        counter = letter_counter.LetterCounter("")
        correct = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
        }
        self.assertEqual(counter.count(), correct)

    def test_count_text(self):
        text = "The quick brown fox jumps over the lazy dog"
        counter = letter_counter.LetterCounter(text)
        correct = {
            "a": 1,
            "b": 1,
            "c": 1,
            "d": 1,
            "e": 3,
            "f": 1,
            "g": 1,
            "h": 2,
            "i": 1,
            "j": 1,
            "k": 1,
            "l": 1,
            "m": 1,
            "n": 1,
            "o": 4,
            "p": 1,
            "q": 1,
            "r": 2,
            "s": 1,
            "t": 2,
            "u": 2,
            "v": 1,
            "w": 1,
            "x": 1,
            "y": 1,
            "z": 1,
        }
        self.assertEqual(counter.count(), correct)

    def test_count_text_with_nonalphabetic_characters(self):
        text = "The quick, brown fox jumps over the lazy dog!"
        counter = letter_counter.LetterCounter(text)
        correct = {
            "a": 1,
            "b": 1,
            "c": 1,
            "d": 1,
            "e": 3,
            "f": 1,
            "g": 1,
            "h": 2,
            "i": 1,
            "j": 1,
            "k": 1,
            "l": 1,
            "m": 1,
            "n": 1,
            "o": 4,
            "p": 1,
            "q": 1,
            "r": 2,
            "s": 1,
            "t": 2,
            "u": 2,
            "v": 1,
            "w": 1,
            "x": 1,
            "y": 1,
            "z": 1,
        }
        self.assertEqual(counter.count(), correct)

    def test_count_text_with_custom_alphabet(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz!'
        text = "The quick, brown fox jumps over the lazy dog!"
        counter = letter_counter.LetterCounter(text, alphabet=alphabet)
        correct = {
            "a": 1,
            "b": 1,
            "c": 1,
            "d": 1,
            "e": 3,
            "f": 1,
            "g": 1,
            "h": 2,
            "i": 1,
            "j": 1,
            "k": 1,
            "l": 1,
            "m": 1,
            "n": 1,
            "o": 4,
            "p": 1,
            "q": 1,
            "r": 2,
            "s": 1,
            "t": 2,
            "u": 2,
            "v": 1,
            "w": 1,
            "x": 1,
            "y": 1,
            "z": 1,
            "!": 1
        }
        self.assertEqual(counter.count(), correct)


if __name__ == '__main__':
    unittest.main()
