import unittest
from crypto_tools.stats import letter_frequency


class TestLetterFrequency(unittest.TestCase):
    def test_count_empty(self):
        counter = letter_frequency.LetterFrequency("")
        self.assertEqual(counter.calculate(), {})

    def test_count_text(self):
        text = "The quick brown fox jumps over the lazy dog"
        counter = letter_frequency.LetterFrequency(text).calculate()
        print(counter["a"])
        self.assertTrue(0.0285 <= counter["a"] <= 0.0286)
        self.assertTrue(0.0057 <= counter["t"] <= 0.0058)


if __name__ == '__main__':
    unittest.main()
