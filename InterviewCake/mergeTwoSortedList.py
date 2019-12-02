import unittest

"""
In order to wind the prize for most cookies sold,
my friend Alice and I are going to merge our Girl Scout
Cookies orders and enter as one unit.

Our lists are sorted numerically in lists.
Write a function to merge our lists of orders into one sorted list.
"""

# Time: O(n) | Space: O(n)

def merge_lists(list_a, list_b):
    if len(list_a) == 0:
        return list_b
    if len(list_b) == 0:
        return list_a
    
    a_idx = b_idx = 0
    result = []
    while a_idx < len(list_a) and b_idx < len(list_b):

        if list_a[a_idx] < list_b[b_idx]:
            result.append(list_a[a_idx])
            a_idx += 1
            if a_idx == len(list_a):
                return result + list_b[b_idx:]
                break
            continue
        if list_b[b_idx] < list_a[a_idx]:
            result.append(list_b[b_idx])
            b_idx += 1
            if b_idx == len(list_b):
                return result + list_a[a_idx:]
                break
            continue
        if list_b[b_idx] == list_a[a_idx]:
            result.append(list_a[a_idx])
            result.append(list_b[b_idx])
            a_idx += 1
            if a_idx == len(list_a):
                return result + list_b[b_idx:]
                break
            b_idx += 1
            if b_idx == len(list_b):
                return result + list_a[a_idx:]
                break
            continue
    
    return result


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)


    