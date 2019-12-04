
import unittest

# Write a function that finds the best profit from the sale of one apple stock
# Time: O(n) | Time: O(1)
def get_max_profit(stock_prices):
    
    # If there is no stock or only one stock, raise an exception, because you cannot buy and sell
    if len(stock_prices) == 0 or len(stock_prices) == 1:
        raise Exception
    
    # Your current stock will always be the first stock price you can obtain
    current_stock = stock_prices[0]
    # And your best profit is the first stock you have and you sell the next day
    best_profit = stock_prices[1] - current_stock

    for i in range(1, len(stock_prices)-1):
        # If you obtain the stock today and sell tomorrow and its higher, change your current stock to this stock
        if stock_prices[i+1] - stock_prices[i] > best_profit:
            current_stock = stock_prices[i]
            best_profit = stock_prices[i+1] - stock_prices[i]
        # If you can profit more by selling your current stock on the next day, then dont change your stock, 
        # but sell on the next day instead, and update the profit
        elif stock_prices[i+1] - current_stock > best_profit:
            best_profit = stock_prices[i+1] - current_stock
        # If your past profits are always higher than buying stock today and sell tmr or hold current stock and sell tmr, do nothing
        else:
            continue
    
    return best_profit


# Tests
class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)
