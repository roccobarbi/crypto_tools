from string import whitespace


def has_whitespace(text):
    for character in text:
        if character in whitespace:
            return True
    return False
