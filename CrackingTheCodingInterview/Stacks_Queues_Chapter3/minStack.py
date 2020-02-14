
# Design a stack that has a min fuction that returns the minimum value of the stack, in addition to pop and push

class StackNode:
    def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.min = []

    # Time: O(1)
    def pop(self):
        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.next

        return data

    # Time: O(1)
    def push(self, data):
        newNode = StackNode(data)
        
        newNode.next = self.top
        self.top = newNode
        
        if len(self.min) == 0:
            self.min.append(newNode.data)
        else:
            if newNode.data < self.min[-1]:
                self.min.append(newNode.data)
            else:
                self.min.append(self.min[-1])

    # Time: O(1)
    def getMin(self):
        if len(self.min) == 0:
            return None
        return self.min[-1]

    def remove(self):
        if self.top is None:
            self.min = None
            return None
        data = self.top.data
        self.top = self.top.next
        # remove the rightmost element in the array aka the minimum value
        self.min.pop()

        return data
    
    # Time: O(1)
    def peek(self):
        return self.top
    

stack = Stack()
stack.push(2)
stack.push(1)
stack.push(3)

print(stack.getMin())
# Expected: 1

stack.remove()
stack.remove()

print(stack.getMin())
# Expected: 2


