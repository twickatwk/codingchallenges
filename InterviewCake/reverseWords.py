import unittest
# Write a function that takes a list of characters 
# and reverses the order of the words in place.

# Time: O(n) | Space: O(1)
def reverse_words(array):
    
    start = 0

    reverse_words_helper(array, 0, len(array)-1)
    
    for i in range(len(array)):
        if array[i] == " ":
            reverse_words_helper(array, start, i-1)
            start = i+1
        if i == len(array) - 1:
            reverse_words_helper(array, start, i)
    
    #print(array)

def reverse_words_helper(array, start, end):
    left_index = start
    right_index = end

    while left_index < right_index:
        array[left_index], array[right_index] = array[right_index], array[left_index]
        left_index += 1
        right_index -= 1
    return array








# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)