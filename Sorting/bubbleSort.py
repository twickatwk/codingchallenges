
# This piece of code defines a bubble sort.
# Explaination:
# The larger element will always be bubbling up, so after the first interation of the outer loop, 
# the first largest element will now be at the last position of the array

# Time: O(N^2) | Space: O(1)
def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    print(array)


bubbleSort([1,5,2,7,5])