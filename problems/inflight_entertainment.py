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

    movie_lengths_seen = set()

    # O(n) solution
    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    return False


if __name__ == "__main__":
    result = can_two_movies_fill_flight([4, 3, 2], 5)
    print("result {}".format(result))
