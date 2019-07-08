from typing import List


class WordCloudData():
    """Class to create a word cloud dict from input string"""

    def __init__(self, input_string: str) -> None:
        self.word_to_counts = {}

        tokens = self.split_words(input_string)

        # Runtime and space cost O(n)
        for token in tokens:
            if token in self.word_to_counts:
                self.word_to_counts[token] += 1
            else:
                self.word_to_counts[token] = 1

    def split_words(self, input_string: str) -> List:
        """Splits a sentence into list of words containing only alpha numeric
        chars

        Args:
            input_string: input sentence

        Returns:
            List of words with only alpha chars
        """

        tokens = input_string.split(" ")
        return [token if token[-1].isalpha() else token[0:-1]
                for token in tokens]


if __name__ == "__main__":
    input_string = 'Mmm...mmm...decisions...decisions'

    result = WordCloudData(input_string)
    print("Result: {}".format(result.word_to_counts))
