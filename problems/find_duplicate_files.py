import os
from typing import List, Tuple

Duplicates = List[Tuple(str, str)]


def find_duplicate_files(starting_dir: str) -> Duplicates:
    """Searches through file systems looking for duplicate files

    Args:
        starting_dir: file path of the directory to search through

    Returns
        list of duplicate file path pairs
    """
    pass


if __name__ == "__main__":
    result = find_duplicate_files()
    print(f"result -> {result}")
