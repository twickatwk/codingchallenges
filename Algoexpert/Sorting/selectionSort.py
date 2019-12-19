

# Time: O(N^2) | Space: O(1)
# Easy
# Selection Sort Logic
# Find the smallest value in the unsorted list, and place it in the first position of the sorted list in the array
# Find next smallest value from i + 1, and it will be placed into the second position of the sorted list
def selectionSort(array):
    # N-1 number of swaps/search to perform
    for i in range(len(array)-1):
        # The smallest value will be initiatized to the current value of i
        smallestIndex = i
        minValue = array[i]

        # Search the smallest value from position i onwards
        for j in range(i, len(array)):
            if array[j] < minValue:
                minValue = array[j]
                smallestIndex = j
        
        # Swap the smallest value of the unsorted list with the current position of i
        array[i], array[smallestIndex] = array[smallestIndex], array[i]
    
    return array

print(selectionSort([8, 5, 2, 9, 5, 6, 3]))