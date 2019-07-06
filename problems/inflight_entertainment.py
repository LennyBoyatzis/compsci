from typing import List


def can_two_movies_fill_flight(movie_lengths: List,
                               flight_length: int) -> bool:
    """Determines whether there are two movies whose length is equal to flight
    length

    Args:
        flight_length: Length of the flight in minutes
        movie_lengths: List of movie durations

    Returns: Boolean indicating whether there are two movies whose length is
    equal to that of the flight
    """

    # Timsort: O(nlogn) worst case
    sorted_movie_lengths = sorted(movie_lengths)

    # Single for loop O(n)
    for index, value in enumerate(sorted_movie_lengths):
        if index is not len(sorted_movie_lengths) - 1:
            if sorted_movie_lengths[index + 1] + value == flight_length:
                return True
    return False


if __name__ == "__main__":
    result = can_two_movies_fill_flight([4, 3, 2], 5)
    print("result {}".format(result))
