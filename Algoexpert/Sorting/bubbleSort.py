
# https://www.algoexpert.io/questions/Bubble%20Sort

# Easy
# Time: O(N^2) | Space: O(1)
def bubbleSort(array):

    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array


print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))