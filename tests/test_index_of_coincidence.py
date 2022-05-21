import unittest

from crypto_tools.stats import index_of_coincidence


class TestIndexOfCoincidence(unittest.TestCase):
    def test_create_empty(self):
        try:
            ic_counter = index_of_coincidence.IndexOfCoincidence("")
            self.fail("Did not raise exception creating IndexOfCoincidence with "
                "empty text!")
        except ValueError:
            pass

    def test_calculate_ic_fox(self):
        text = ("The quick brown fox jumps over the lazy dog")
        ic = index_of_coincidence.IndexOfCoincidence(text).calculate()
        print(str(ic))
        self.assertGreater(ic, 0.0217, "Index of coincidence too low!")
        self.assertLess(ic, 0.0219, "Index of coincidence too high!")

    def test_calculate_ic(self):
        text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam "
            "mattis non turpis eu imperdiet. Nulla rhoncus, augue vitae ultrices "
            "feugiat, orci velit semper lorem, ac sodales arcu velit ac mi. "
            "Maecenas varius finibus rhoncus. Vestibulum lacus augue, viverra nec "
            "aliquet quis, hendrerit.")
        ic = index_of_coincidence.IndexOfCoincidence(text).calculate()
        print(str(ic))
        self.assertGreater(ic, 0.0677, "Index of coincidence too low!")
        self.assertLess(ic, 0.0678, "Index of coincidence too high!")
