
# https://www.algoexpert.io/questions/Insertion%20Sort

# Time: O(N^2) | Space: O(1)

# Insertion Sort Explaination:
# Maintains two different sublist in the array, left side is sort, and right side is unsorted.
# Sorted list starts from len 1, and pick the first unsorted value from the unsorted list on the right
# Check where the unsorted value lies in the sorted side of the array, by checking one at a time, 
# Shift values in the sorted side to the right, as long as the unsorted value is still smaller than the current value
def insertionSort(array):

    # Picks the unsorted value N-1 times to check where it lies
    for i in range(len(array)-1):

        current = i+1
        # The first len of the sorted array will always be 1, and increases to N-1 after.
        for j in range(current):
            # For each value in the sorted list, compare it with the unsorted value, if the unsorted value is smaller:
            if array[current-j] < array[current-j-1]:
                # You will have to swap the current unsort and sorted value's position
                array[current-j], array[current-j-1] = array[current-j-1], array[current-j]
            else:
                break
    
    return array
    
    

print(insertionSort([8, 5, 2, 9, 5]))