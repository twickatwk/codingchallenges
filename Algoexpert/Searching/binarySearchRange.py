
# https://www.algoexpert.io/questions/Search%20For%20Range

# Hard

# Time: O(Log N) | Space: O(1)
def searchForRange(array, target):

    lower = 0
    upper = len(array) - 1
    # O(Log N) # searches for the left most extrene point - variant of binary search
    left = searchLeftExtreme(array, lower, upper, target, True)
    # O(Log N) # searches for the right most extreme point - variant of binary search
    right = searchLeftExtreme(array, lower, upper, target, False)

    return [left, right]

def searchLeftExtreme(array, lower, upper, target, searchLeft):

    # Checks whether the left point has exceed the right pointer, if not, continue the search
    while lower + 1 < upper:
        
        mid = (lower+upper) // 2

        # When you find the target, you whether its the most edge of the range of the target
        if array[mid] == target:

            # Check if its the left extreme of the target value

            if searchLeft:

                # If it is not the left most point of the target, update the upper bound, and continue the search
                if array[mid-1] == array[mid]:

                    upper = mid-1
                    continue

                else:

                    # If it is the left most point, return the index
                    return mid

            # Checks if its the right most point of the target
            else:

                # If it is not the right most point of the target, update the lower bound, and continue the search
                if array[mid+1] == array[mid]:

                    lower = mid+1
                    continue
                # If it is the right most point of the target, return the index
                else:
                    return mid

        # Otherwise, continue your normal binary search
        if target > array[mid]:
            lower = mid + 1
        
        if target < array[mid]:
            upper = mid - 1
    
    if target == array[lower]:
        return lower
    if target == array[upper]:
        return upper
    
    return -1



print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))
    