from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе

    >>> encode('SOS')
    '... ---     ...'
    >>> encode('FIRST TASK')  # doctest: +ELLIPSIS
    '..-. ... -.-'
    >>> encode('a')  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    KeyError: 'a'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
