
# https://www.algoexpert.io/questions/Min%20Heap%20Construction

# Easy

# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:

    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # Time: O(N)
    def buildHeap(self, array):
        # Write your code here.
        for i in range(len(array)-1, -1, -1):
            self.siftDown(i, array)
        
        return array

    # Time: O(Log N)
    def siftDown(self, index, array):
        # Write your code here.
        
        # Base case - if there is no first child, return, because its the leaf node/last parent
        if 2*index+1 >= len(array):
            return
        # If only one child exists, compare the one child
        if 2*index+2 >= len(array):
            if array[2*index+1] < array[index]:
                # If the first child is smaller than the parent, swap them
                array[2*index+1], array[index] = array[index], array[2*index+1]
                self.siftDown(2*index+1,array)
        if 2*index+2 >= len(array):
            return
        
        # If there are two child, compare two child
        if array[2*index+1] < array[index] and array[2*index+2] < array[index]:
            if array[2*index+1] < array[2*index+2]:
                array[index], array[2*index+1] = array[2*index+1], array[index]
                self.siftDown(2*index+1, array)
            else:
                array[index], array[2*index + 2] = array[2*index+2], array[index]
                self.siftDown(2*index+2, array)
                
        if array[2*index+1] < array[index]:
            array[index], array[2*index+1] = array[2*index+1], array[index]
            self.siftDown(2*index+1, array)
        if array[2*index+2] < array[index]:
            array[index], array[2*index + 2] = array[2*index+2], array[index]
            self.siftDown(2*index+2, array)
        
        return

    # Time: O(Log N)
    def siftUp(self, index, array):
        # Write your code here.
        
        # Base case - If there are no more parent at the top
        parentIndex = (index-1)//2
        if parentIndex < 0:
            return
        
        # If the parent is larger then the current child, you need to swap them
        if array[parentIndex] > array[index]:
            array[parentIndex], array[index] = array[index], array[parentIndex]
            self.siftUp(parentIndex, array)
        
        return

    # Time: O(1)
    def peek(self):
        # Write your code here.
        return self.heap[0]

    # Time: O(Log N)
    def remove(self):
        # Write your code here.
        
        # Swap the root element with the last element in the array
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        # Remove the last element in the heap
        self.heap.pop()
        # Sift down the root node to the correct position
        self.siftDown(0, self.heap)
        
        return

    # Time: O(Log N)
    def insert(self, value):
        # Write your code here.
        
        # Add the value into the last element of the heap
        self.heap.append(value)
        # Sift the element at the last position to the correct position
        self.siftUp(len(self.heap)-1,self.heap)
		
