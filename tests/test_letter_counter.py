import unittest
from crypto_tools.stats import letter_counter


class TestLetterCounter(unittest.TestCase):
    def test_count_empty(self):
        counter = letter_counter.LetterCounter("")
        self.assertEqual(counter.count(), {})

    def test_count_text(self):
        text = "The quick brown fox jumps over the lazy dog"
        counter = letter_counter.LetterCounter(text).count()
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
        self.assertEqual(counter, correct)


if __name__ == '__main__':
    unittest.main()
