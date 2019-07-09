from typing import List


def sort_scores(unsorted_scores: List,
                highest_possible_score: int) -> List:
    """Sorts a list of scores in descending order

    Args:
        unsorted_scores: list of unsorted scores
        highest_possible_score: limit on the highest possible score

    Returns a sorted list in descending order
    """
    pass


if __name__ == "__main__":
    actual = sort_scores([30, 60], 100)
    print("Actual: {}".format(actual))
