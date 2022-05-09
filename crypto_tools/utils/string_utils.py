from string import whitespace


def has_whitespace(text):
    for character in text:
        if character in whitespace:
            return True
    return False


def includes_other_letters(text, allowed):
    for character in text:
        if character not in allowed:
            return True
    return False
