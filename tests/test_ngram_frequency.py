import unittest
from crypto_tools.stats import ngram_frequency


class TestNgramFrequency(unittest.TestCase):
    def test_count_empty(self):
        counter = ngram_frequency.NgramFrequency("")
        self.assertEqual(counter.calculate(), {})

    def test_count_text(self):
        text = "The quick brown fox jumps over the lazy dog"
        counter = ngram_frequency.NgramFrequency(text).calculate()
        print(counter["a"])
        self.assertTrue(0.058 <= counter["th"] <= 0.059)
        self.assertTrue(0.029 <= counter["t"] <= 0.030)


if __name__ == '__main__':
    unittest.main()
