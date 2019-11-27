
# This piece of code defines a selection sort
# Explaination:
# At each outer loop interation, the max value will be selected, and be placed at the furthest possible point
# this means that, in the first iteration, the furthest place to put the first value will be the last position,
# decrementing by 1 each time the outer loop runs.

# Time: O(N^2) | Space: O(1)
def selectionSort(array):
    largestValue = None
    index = None
    for i in range(len(array)-1):
        largestValue = array[0]
        index = 0
        for j in range(len(array)-i):
            if array[j] > largestValue:
                largestValue = array[j]
                index = j
        array[index], array[len(array)-1-i] =  array[len(array)-1-i], array[index]
        print(array)

selectionSort([7,8,5,9,3,2])
