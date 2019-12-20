# https://www.algoexpert.io/questions/Continuous%20Median
# Hard

# O(Log N) | Space: O(N)
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        # Lower Half - Max Heap
        self.lowerHalf = []
        
        # Greater Half - Min Heap
        self.greaterHalf = []
        
    def swapNodes(self, i, j, array):
        array[i], array[j] = array[j], array[i]

    def minHeapSiftUp(self, index):
        
        parentNode = (index-1)//2
        if parentNode < 0:
            return
        
        if self.greaterHalf[index] < self.greaterHalf[parentNode]:
            self.swapNodes(index, parentNode, self.greaterHalf)
            self.minHeapSiftUp(parentNode)

    def minHeapSiftDown(self, index):
        childOneIndex = 2*index+1
        childTwoIndex = 2*index+2
        
        
        # If there is no child, just return
        if childOneIndex >= len(self.greaterHalf):
            return
        
        childOne = self.greaterHalf[childOneIndex]
        
        
        # If there is only one child
        if childTwoIndex >= len(self.greaterHalf):
            if self.greaterHalf[index] > self.greaterHalf[childOneIndex]:
                self.swapNodes(index, childOneIndex, self.greaterHalf)
                self.minHeapSiftDown(childOneIndex)
        
        if childTwoIndex >= len(self.greaterHalf):
            return
        
        childTwo = self.greaterHalf[childTwoIndex]
        
        # Compare if there are two children
        if childOne < self.greaterHalf[index] and childTwo < self.greaterHalf[index]:
            # Swap the largest one between the two child
            if childOne < childTwo:
                self.swapNodes(childOneIndex, index, self.greaterHalf)
                self.minHeapSiftDown(childOneIndex)
            else:
                self.swapNodes(childTwoIndex, index, self.greaterHalf)
                self.minHeapSiftDown(childTwoIndex)
        if childOne < self.greaterHalf[index]:
            self.swapNodes(childOneIndex, index, self.greaterHalf)
            self.minHeapSiftDown(childOneIndex)
        if childTwo < self.greaterHalf[index]:
            self.swapNodes(childTwoIndex, index, self.greaterHalf)
            self.minHeapSiftDown(childTwoIndex)
        
        return

    def minHeapInsert(self, number):
        self.greaterHalf.append(number)
        self.minHeapSiftUp(len(self.greaterHalf)-1)

    def minHeapRemove(self):
        # Swap the root node with the last element in the heap
        self.swapNodes(0, len(self.greaterHalf) - 1, self.greaterHalf)
        
        nodeToRemove = self.greaterHalf[-1]
        self.greaterHalf.pop()
        
        self.minHeapSiftDown(0)
        
        return nodeToRemove


    def maxHeapSiftUp(self, index):
        
        parentNode = (index-1)//2
        if parentNode < 0:
            return
        
        if self.lowerHalf[index] > self.lowerHalf[parentNode]:
            self.swapNodes(index, parentNode, self.lowerHalf)
            self.maxHeapSiftUp(parentNode)

    def maxHeapSiftDown(self, index):
        childOneIndex = 2*index+1
        childTwoIndex = 2*index+2
        
        
        # If there is no child, just return
        if childOneIndex >= len(self.lowerHalf):
            return
        
        childOne = self.lowerHalf[childOneIndex]
        
        
        # If there is only one child
        if childTwoIndex >= len(self.lowerHalf):
            if self.lowerHalf[index] < self.lowerHalf[childOneIndex]:
                self.swapNodes(index, childOneIndex, self.lowerHalf)
                self.maxHeapSiftDown(childOneIndex)
        
        if childTwoIndex >= len(self.lowerHalf):
            return
        
        childTwo = self.lowerHalf[childTwoIndex]
        
        # Compare if there are two children
        if childOne > self.lowerHalf[index] and childTwo > self.lowerHalf[index]:
            # Swap the largest one between the two child
            if childOne > childTwo:
                self.swapNodes(childOneIndex, index, self.lowerHalf)
                self.maxHeapSiftDown(childOneIndex)
            else:
                self.swapNodes(childTwoIndex, index, self.lowerHalf)
                self.maxHeapSiftDown(childTwoIndex)
        if childOne > self.lowerHalf[index]:
            self.swapNodes(childOneIndex, index, self.lowerHalf)
            self.maxHeapSiftDown(childOneIndex)
        if childTwo > self.lowerHalf[index]:
            self.swapNodes(childTwoIndex, index, self.lowerHalf)
            self.maxHeapSiftDown(childTwoIndex)
        
        return
        
        
            

    def maxHeapInsert(self, number):
        self.lowerHalf.append(number)
        self.maxHeapSiftUp(len(self.lowerHalf)-1)
        
        
    def maxHeapRemove(self):
        # Swap the root node with the last element in the heap
        self.swapNodes(0, len(self.lowerHalf) - 1, self.lowerHalf)
        
        nodeToRemove = self.lowerHalf[-1]
        self.lowerHalf.pop()
        
        self.maxHeapSiftDown(0)
        
        return nodeToRemove
        
    # O(Log N) | Space: O(N)
    def insert(self, number):
        # Write your code here.
        
        # If its the first element, just put it in the lower half
        if len(self.lowerHalf) == 0:
            self.lowerHalf.append(number)
            self.median = number
            return
        
        if number > self.lowerHalf[0]:
            self.minHeapInsert(number)
            if len(self.greaterHalf) - len(self.lowerHalf) >= 2:
                valueToInsertLowerHalf = self.minHeapRemove()
                self.maxHeapInsert(valueToInsertLowerHalf)
        else:
            self.maxHeapInsert(number)
            if len(self.lowerHalf) - len(self.greaterHalf) >= 2:
                valueToInsertGreaterHalf = self.maxHeapRemove()
                self.minHeapInsert(valueToInsertGreaterHalf)
        
        # Compute the median after every insertion
        if len(self.lowerHalf) == len(self.greaterHalf):
            self.median = (self.lowerHalf[0] + self.greaterHalf[0])/2
        elif len(self.lowerHalf) > len(self.greaterHalf):
            self.median = self.lowerHalf[0]
        else:
            self.median = self.greaterHalf[0]

    def getMedian(self):
        return self.median