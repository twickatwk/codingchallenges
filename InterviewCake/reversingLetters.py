import unittest
# Write a function that takes a list of characters and reverses 
# the letters in-place

# time: O(n) | Space: O(1)
def reverse_letters(array):
    left_index = 0
    right_index = len(array)-1
    while left_index < right_index:
        array[left_index], array[right_index] = array[right_index], array[left_index]
        left_index += 1
        right_index -= 1

reverse_letters(['a', 'b', 'c'])

# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)