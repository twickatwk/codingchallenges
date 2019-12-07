# https://www.interviewcake.com/question/python/highest-product-of-3?course=fc1&section=greedy
# Given a list of integers, find the highest 
# product you can get from three of the integers.
# There is at least 3 integers

# Time: O(n) | Space: O(1)
def highest_product_of_3(list_of_ints):

    if len(list_of_ints) < 3:
        raise ValueError("There must be 3 integers")

    highest_product_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    highest_product_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_2 = highest_product_2
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    for i in range(2, len(list_of_ints)):
        current_num = list_of_ints[i]
        highest_product_3 = max(highest_product_3, highest_product_2 * current_num, lowest_product_2 * current_num)
        highest_product_2 = max(highest_product_2, current_num * highest, current_num * lowest)
        lowest_product_2 = min(lowest_product_2, lowest * current_num, highest *  current_num)
        highest = max(highest, current_num)
        lowest = min(lowest, current_num)
    
    return highest_product_3



print(highest_product_of_3([-5, -1, -3, -2]))