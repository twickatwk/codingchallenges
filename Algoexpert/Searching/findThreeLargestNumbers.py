
# Time: O(N) | Space: O(1)
def findThreeLargestNumbers(array):
    if len(array) < 3:
        return []
    array.sort()
    return array[-3:]

print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))

