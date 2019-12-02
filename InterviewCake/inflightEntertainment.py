import unittest

"""
Write a function that takes an integer flight_length (in minutes) and
a list of integers movie_lengths (in minutes) and returns a boolean
indicating whether there are two numbers in movie_lengths whose sum equals
flight_length
"""

# Time: O(n) | Space: O(n)
# Time - you only go through the list of movie lengths once, and everytime, you check whether the difference (aka pair) exists in the dictionary which only takes constant time
# Space - You only need to store the list of differences between the flight length & movie lengths for retrieval
def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    dict_film_length = {}

    for i in range(len(movie_lengths)):
        difference = flight_length - movie_lengths[i]
        if difference in dict_film_length:
            return True
        else:
            dict_film_length[movie_lengths[i]] = True

    return False

# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = can_two_movies_fill_flight([4, 3, 2], 5)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)
