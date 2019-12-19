
# https://www.algoexpert.io/questions/Quick%20Sort

# Time Complexity - Worst Case: O(N^2) | Average/Best Case: O(N Log N)
# Space Complexity - O(Log N)
def quickSortHelper(array, startIdx, endIdx):
    # Return if array of len 0, starting index must always be smaller than ending index
    if startIdx >= endIdx:
        return

    # The pivot index will always be first value of the current sub array
    pivotIdx = startIdx

    # The left index will be to the right of the starting index
    leftIdx = startIdx + 1
    # Right index starts at the end of the sub array
    rightIdx = endIdx

    # As long as the right index is still equal or greater than the left index, continue
    while rightIdx >= leftIdx:

        # If the left index is larger than the pivot and the right index is smaller than the pivot, swap them both
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
        # If the left index is equal or smaller than the pivot, it's at the correct position, increment the left index
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        # If the right index is equal or greater than the pivot, it's at the correct position, decrement the right index
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    
    # When the process is done, swap the pivot to the correct position, which is the location of the right index
    array[pivotIdx], array[rightIdx] = array[rightIdx], array[pivotIdx]

    # Check which of the two sub arrays are smaller, this is to ensure at most Log N space for the recursive call stack
    leftSubarrayIsSmaller = (rightIdx - 1)-startIdx < endIdx - (rightIdx + 1)

    # Recursively sort the left subarray and the right subarray from the corrected pivot position 
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx-1)
        quickSortHelper(array, rightIdx+1, endIdx)
    else:
        quickSortHelper(array, rightIdx+1, endIdx)
        quickSortHelper(array, startIdx, rightIdx-1)
    

def quickSort(array):
    # starint and ending index is required because you're attempting to perform swap in-place
    quickSortHelper(array, 0, len(array)-1)
    return array

print(quickSort([8, 5, 2, 9, 5, 6, 3]))