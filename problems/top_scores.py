from typing import List
from collections import Counter


def sort_scores(unsorted_scores: List,
                highest_possible_score: int) -> List:
    """Sorts a list of scores in descending order

    Args:
        unsorted_scores: list of unsorted scores
        highest_possible_score: limit on the highest possible score

    Returns a sorted list in descending order
    """

    score_counts = [0] * (highest_possible_score + 1)

    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []

    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        for time in range(count):
            sorted_scores.append(score)
    return sorted_scores


if __name__ == "__main__":
    actual = sort_scores([70, 30, 60, 60, 70], 100)
    print("Actual: {}".format(actual))
