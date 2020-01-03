
# Given a rotated list of words, find the point where the rotation has begun

# Time: O(Log N) - Variant of binary search | Space: O(1)
def findRotationPoint(array):

    lower = 0 
    upper = len(array) - 1
    

    while lower + 1 < upper:
        mid = (lower+upper) // 2

        # If the current value (midpoint) is larger than the lower element and smaller 
        # than the upp element, then you know that the current boundary 
        # is already sorted
        if array[mid] > array[lower] and array[mid] < array[upper]:
            return lower
        
        # If the current value (midpoint) smaller than its left neighbour and 
        # smaller than its right neighbour, then the current midpoint 
        # is the rotation point
        if array[mid] < array[mid+1] and array[mid] < array[mid-1]:
            return mid
        # Otherwise if the value at the midpoint is smaller than the lower point element
        # You know that all the elements on the right of the midpoint is already sorted
        # So start the search on the left instead, by updating the upper boundary to
        # the left of the midpoint
        elif array[mid] < array[lower]:
            upper = mid-1
        else:
            lower = mid+1
    
    if array[upper] < array[lower]:
        return upper
        
    return lower

words = [
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'karpatka',
    'othellolagkage',
]

print(findRotationPoint(words))