# Approach: Using two pointers
# Time: O(N) | Space: O(1)
def moveElementToEnd(array, toMove):
    # Write your code here.

    start = 0
    end = len(array) - 1

    while start < end:
        while array[end] == toMove:
            end -= 1
            if end == start:
                return array
        while array[start] != toMove:
            start += 1
            if end == start:
                return array
        # perform the swap
        array[start], array[end] = array[end], array[start]
        
    return array