import unittest


"""
Given all three lists, write a function to check that the service
is first-come, first-served basis. All food should come out in the order
that customers requested it.

Input:
Take Out Orders: [1, 3, 5]
Dine In Orders: [2, 4, 6]
Served Orders: [1, 2, 3, 5, 4, 6]

Result: True
"""

# Time: O(n) | Space: O(1)
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    a_idx = 0
    b_idx = 0

    if len(take_out_orders) + len(dine_in_orders) != len(served_orders):
        return False

    for i in range(len(served_orders)):

        if a_idx < len(take_out_orders) and served_orders[i] == take_out_orders[a_idx]:
            a_idx += 1
            continue
        elif b_idx < len(dine_in_orders) and served_orders[i] == dine_in_orders[b_idx]:
            b_idx += 1
            continue

        return False
    
    return True


# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)


unittest.main(verbosity=2)

