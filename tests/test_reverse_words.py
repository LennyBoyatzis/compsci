import unittest
from problems.reverse_words import reverse_words


def test_reverse_words():
    message = ['c', 'a', 'k', 'e', ' ',
               'p', 'o', 'u', 'n', 'd', ' '
               's', 't', 'e', 'a', 'l']

    expected = ['s', 't', 'e', 'a', 'l', ' ',
                'p', 'o', 'u', 'n', 'd', ' '
                'c', 'a', 'k', 'e']

    result = reverse_words(message)
    assert result == expected


class Test(unittest.TestCase):
    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)
