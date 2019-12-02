import unittest

"""
Write an efficient function that checks whether any permutation of an input
string is a palindrome.
"""

# Time: O(n) | Space: O(n)
def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome

    dict_letter_count = {}

    for i in range(len(the_string)):
        if the_string[i] in dict_letter_count:
            dict_letter_count[the_string[i]] += 1
        else:
            dict_letter_count[the_string[i]] = 1

    isOddCount = 0

    for value in dict_letter_count.values():
        if value % 2 == 1:
            isOddCount += 1
        else:
            continue

    if isOddCount <= 1:
        return True

    return False

# Approach 2: using set to solve the question
# Time: O(n) | Space: O(n)
def has_palindrome_permutation2(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)
    
    # The string has a palindrome if it has one or zero
    # characters without a pair
    return len(unpaired_characters) <= 1


# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)