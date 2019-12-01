
# This is an implementation of binary search using the iterative approach:

# Time: O(log n) | Space: O(1)
def binarySearch(array, target):
    lower = 0 
    upper = len(array) - 1

    # Continue this process as long as there is a middle element between the two pointers (left and right)
    while lower + 1 < upper:
        distance = (upper - lower) // 2
        middle = lower + distance
        if array[middle] == target:
            return True
        if array[middle] > target:
            upper = middle
            continue
        if array[middle] < target:
            lower = middle
            continue
    
    # When there is no more middle element to check, check the current left and right pointer elements
    if array[lower] == target or array[upper] == target:
        return True
    
    return False

print(binarySearch([1,2, 7, 9], 7))