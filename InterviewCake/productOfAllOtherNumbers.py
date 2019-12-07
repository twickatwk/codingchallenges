# https://www.interviewcake.com/question/python/product-of-other-numbers?course=fc1&section=greedy

# You have a list of integers, and for each index, you want to find the product of every 
# integer except the integer at that index

import unittest

"""
# Approach 1: With division
# Time: O(n) | Space: O(n)
def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    if len(int_list) < 2:
       raise ValueError("There should at least be two numbers in the list")
    
    sum_product = 1
    zeroCounter = 0
    for i in range(len(int_list)):
        if int_list[i] == 0:
            zeroCounter += 1
            continue
        sum_product *= int_list[i]
    
    result = []

    for i in range(len(int_list)):
        if int_list[i] == 0 and zeroCounter == 1:
            result.append(sum_product)
            continue
        if zeroCounter >= 1:
            result.append(0)
        else:
            result.append(sum_product//int_list[i])

    return result
"""

"""
# Approach 2: Using the greedy approach by finding the patterns. Calculating the product so far for elements before index, 
# and elements after index. Solves the question without the use of division
# Time: O(n) | Space: (n)
def get_products_of_all_ints_except_at_index(int_list):

    
    if len(int_list) < 2:
        raise ValueError("There should at least be two numbers")

    products_of_all_ints_before_int = [None] * len(int_list)
    
    products_so_far = 1

    for i in range(len(int_list)):
        products_of_all_ints_before_int[i] = products_so_far
        products_so_far *= int_list[i]
    
    # This array can actually be reduced but just using the same array as above
    products_of_all_ints_after_int = [None] * len(int_list)

    product_so_far = 1
    for i in range(len(int_list)-1, -1, -1):
        products_of_all_ints_after_int[i] = product_so_far
        product_so_far *= int_list[i]
    
    result = []

    for i in range(len(int_list)):
        result.append(products_of_all_ints_before_int[i] * products_of_all_ints_after_int[i])

    return result
"""

# Approach 3: Using same greedy approach by finding the patterns. Calculating the product so far for elements before index, 
# and elements after index. Solves the question without the use of division. But now with lesser space, by reusing the same list of
# stored products_so_far

# Time: O(n) | Space: (n)
def get_products_of_all_ints_except_at_index(int_list):

    
    if len(int_list) < 2:
        raise ValueError("There should at least be two numbers")

    products_of_all_ints_before_int = [None] * len(int_list)
    
    products_so_far = 1

    for i in range(len(int_list)):
        products_of_all_ints_before_int[i] = products_so_far
        products_so_far *= int_list[i]

    product_so_far = 1
    for i in range(len(int_list)-1, -1, -1):
        products_of_all_ints_before_int[i] = products_of_all_ints_before_int[i] * product_so_far
        product_so_far *= int_list[i]

    return products_of_all_ints_before_int


# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])



unittest.main(verbosity=2)
