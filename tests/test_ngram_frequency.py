import unittest
from crypto_tools.stats import ngram_frequency


class TestNgramFrequency(unittest.TestCase):
    def test_count_empty(self):
        counter = ngram_frequency.NgramFrequency(text="")
        self.assertEqual(counter.calculate(), {})

    def test_count_text(self):
        text = "The quick brown fox jumps over the lazy dog"
        counter = ngram_frequency.NgramFrequency(text=text).calculate()
        self.assertTrue(0.058 <= counter["th"] <= 0.059)

    def test_count_unjoined_text(self):
        text = "The quick brown fox jumps over the lazy dog"
        counter = ngram_frequency.NgramFrequency(text=text, joined=False).calculate()
        self.assertTrue(0.076 <= counter["th"] <= 0.077)


if __name__ == '__main__':
    unittest.main()
