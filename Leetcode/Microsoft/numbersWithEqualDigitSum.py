
# write a function that given an array A consisting of N integers, returns the maximum sum of two numbers whose digits add up to an equal sum. If there are no two numbers whose digits have an equal sum, the function should return -1

# Time: O(N Log N) | Space: O(N)
def numbersWithEqualDigitSum(A):

    # Time: O(N Log N) 
    A.sort(reverse=True)
    
    dictSum = {}
    # Time: O(N)
    for i in range(len(A)):
        digit_string = list(str(A[i]))
        digits = list(map(int, digit_string))
        digitSum = sum(digits)
        # the first sum of digits that exists if the largest sum of pairs with the same sum of digits,
        # because the array is already sorted
        if digitSum in dictSum:
            return dictSum[digitSum] + A[i]
        else:
            dictSum[digitSum] = A[i]

    return -1

print(numbersWithEqualDigitSum([42, 33, 60]))
