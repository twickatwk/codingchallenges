# Write a function that implements merge sort recursively

# Time: O(n log n) | Space: O(n)
def mergeSort(array):
    mergeSortHelper(array)
    
    return array

def mergeSortHelper(array):
    if len(array) == 1:
        return
    
    mid = len(array) // 2
    left = array[0:mid]
    right = array[mid:len(array)]

    mergeSortHelper(left)
    mergeSortHelper(right)

    merge(left, right, array)

def merge(left, right, array):

    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    
    # Checking whether there are leftover left / right arrays after one of them runs out
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

print(mergeSort([5,6,2,1,4]))

