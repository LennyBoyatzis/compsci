import os
from typing import List, Tuple

Duplicates = List[Tuple[str, str]]


def find_duplicate_files(starting_dir: str) -> Duplicates:
    """Searches through file systems looking for duplicate files

    Args:
        starting_dir: file path of the directory to search through

    Returns
        list of duplicate file path pairs
    """

    return os.listdir(starting_dir)


if __name__ == "__main__":
    working_dir = os.getcwd()
    starting_dir = os.path.join(working_dir, 'data')
    result = find_duplicate_files(starting_dir)
    print(f"result -> {result}")
