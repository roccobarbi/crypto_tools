from ..data.index_of_coincidence_by_language import index_of_coincidence_by_language
from ..stats.index_of_coincidence import IndexOfCoincidence


def _ic_estimate(text):
    probable_language = None
    difference = None
    ic_calculator = IndexOfCoincidence(text)
    ic = ic_calculator.calculate()
    for language in index_of_coincidence_by_language:
        if probable_language is None:
            probable_language = language
            difference = abs(ic - index_of_coincidence_by_language[language])
        else:
            if abs(ic - index_of_coincidence_by_language[language]) < difference:
                probable_language = language
                difference = abs(ic - index_of_coincidence_by_language[language])
    return {
        'language': language,
        'index_of_coincidence': ic,
        'index_of_coincidence_of_language': index_of_coincidence_by_language[language]
    }


METHODS = [
    {
        'id': 'ic',
        'name': 'index of coincidence',
        'estimate': _ic_estimate
    }
]


class LanguageEstimator:
    def __init__(self, text, methods):
        self.text = text
        self.methods = []
        for method in methods:
            if method in METHODS.keys():
                self.methods.append(METHODS[method])
            else:
                raise ValueError("Unknown estimation method: " + method)

    def estimate(self):
        estimates = {}
        for method in self.methods:
            estimates[method['id']] = {
                'id': method['id'],
                'name': method['name'],
                'estimate': method['estimate'](self.text)
            }
