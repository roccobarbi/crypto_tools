import unittest
from crypto_tools.stats import ngram_counter


class TestNgramCounter(unittest.TestCase):
    def test_count_empty(self):
        counter = ngram_counter.NgramCounter(text="")
        self.assertEqual(counter.count(), {})

    def test_count_text(self):
        text = "The quick brown fox jumps over the lazy dog"
        counter = ngram_counter.NgramCounter(nvalue=2, text=text).count()
        correct = {
            "th": 2,
            "he": 2,
            "eq": 1,
            "qu": 1,
            "ui": 1,
            "ic": 1,
            "ck": 1,
            "kb": 1,
            "br": 1,
            "ro": 1,
            "ow": 1,
            "wn": 1,
            "nf": 1,
            "fo": 1,
            "ox": 1,
            "xj": 1,
            "ju": 1,
            "um": 1,
            "mp": 1,
            "ps": 1,
            "so": 1,
            "ov": 1,
            "ve": 1,
            "er": 1,
            "rt": 1,
            "el": 1,
            "la": 1,
            "az": 1,
            "zy": 1,
            "yd": 1,
            "do": 1,
            "og": 1,
        }
        self.assertEqual(counter, correct)


if __name__ == '__main__':
    unittest.main()
