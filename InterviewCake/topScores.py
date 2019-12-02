import unittest
"""
    Write a function that takes:
    1. a list of unsorted_scores
    2. the highest_possible_score in the game
    and returns a sorted list of scores in less than O(n log n)
"""

# Time: O(n) | Space: O(n)
# Explaination:
# Counting Approach
# Notice what those loops iterate over. The outer loop runs once for each unique number
# in the list. The inner loop runs once for each time that number occured.
# Another way to look at it: in each iteration of our two nested loop, we append one item
# to sorted_scores. How many numbers end up in sorted_scores in the end? Exactly how many were in the input list! n
def sort_scores(unsorted_scores, highest_possible_score):

    # List of 0s at indices 0..highest_possible_score
    score_counts = [0] * (highest_possible_score+1)
    
    # Populate score_counts
    for score in unsorted_scores:
        score_counts[score] += 1
    
    # Populate the final sorted list
    sorted_scores = []

    # For each item in score_counts
    for score in range(len(score_counts)-1, -1, -1):
        count = score_counts[score]

        # For the number of times the item occurs
        for i in range(count):
            sorted_scores.append(score)
    
    return sorted_scores





















# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)