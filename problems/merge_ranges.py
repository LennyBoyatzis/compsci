from typing import List, Tuple


def merge_ranges(ranges: List[Tuple]) -> List[Tuple]:
    """Calculates a condensed list of meeting time ranges

    Args:
        ranges: Uncondensed list of meeting time ranges

    Returns:
        Condensed list of meeting time ranges
    """

    sorted_meetings = sorted(ranges, key=lambda tup: tup[0])
    merged_meetings = []

    for index, meeting in enumerate(sorted_meetings):
        if len(sorted_meetings) - 1 == index:
            print("meeting", meeting)
            return


if __name__ == "__main__":
    ranges = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    merge_ranges(ranges)

