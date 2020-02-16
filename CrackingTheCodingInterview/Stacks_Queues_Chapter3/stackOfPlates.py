
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# each of the stack has a specific capacity
class Stack:
    def __init__(self):
        self.top = None
        self.currentSize = 0
        self.capacity = 3
    
    def push(self, data):
        # everytime when you try to add elements to the stack, check whether it exceeds the capacity
        if self.currentSize == self.capacity:
            return False
        
        newNode = StackNode(data)
        newNode.next = self.top
        self.top = newNode
        self.currentSize += 1

        return True

    def isFull(self):
        return self.capacity == self.currentSize

    def pop(self):
        if self.top is None:
            return False
        data = self.top.data
        self.top = self.top.next
        self.currentSize -= 1
    
    def peek(self):
        return self.top.data

    def isEmpty(self):
        return self.top is None


class StackOfPlates:
    def __init__(self):
        self.stackOfPlates = []
    
    # Time: O(1)
    def putPlate(self, data):
        if len(self.stackOfPlates) == 0:
            stack = Stack()
            stack.push(data)
            self.stackOfPlates.append(stack)
        else:
            # if an exiting stack of plates exists, take the last stack
            lastStack = self.stackOfPlates[-1]
            if not lastStack.isFull():
                lastStack.push(data)
            else:
                newstack = Stack()
                newstack.push(data)
                self.stackOfPlates.append(newstack)
    
    # Time: O(1)
    def removePlate(self):
        if len(self.stackOfPlates) == 0:
            return False
        
        # take the lastStack of plates
        lastStack = self.stackOfPlates[-1]
        lastStack.pop()
        if lastStack.top is None:
            self.stackOfPlates.pop()
    
    # Time: O(S)
    def returnAllPlates(self):
        print("Size of Stacks: " + str(len(self.stackOfPlates)))
        for stack in self.stackOfPlates:
            head = stack.top
            while head is not None:
                print(head.data)
                head = head.next
        


"""            
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.isFull())
stack.push(3)
print(stack.peek())
# it will not push any elements into the stack once it reaches its capacity
stack.push(4)
print(stack.peek())
stack.pop()
stack.push(4)
print(stack.peek())
"""

stack = StackOfPlates()
stack.putPlate(1)
stack.returnAllPlates()
stack.putPlate(2)
stack.putPlate(3)
stack.returnAllPlates()
stack.putPlate(3)
stack.returnAllPlates()
stack.removePlate()
stack.returnAllPlates()






