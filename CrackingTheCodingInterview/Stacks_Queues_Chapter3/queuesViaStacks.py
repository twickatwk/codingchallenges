
# Implement a Queue using two Stacks

# definition of a stack node
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# definition of a stack class
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        
        newNode = StackNode(data)
        newNode.next = self.top
        self.top = newNode
    
    def pop(self):

        if self.top is None:
            return None
        
        data = self.top.data

        self.top = self.top.next

        return data
    
    def peek(self):
        return self.top.data

    def isEmpty(self):
        return self.top is None

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.head = None
    
    # Time: O(1)
    def enqueue(self, data):
        # if the stack is None, set it to the head of the queue
        if self.head is None:
            self.head = data
        
        self.stack1.push(data)
    
    # Time: O(N)
    def dequeue(self):
        while self.stack1.top is not None:
            self.stack2.push(self.stack1.pop())
        
        data = self.stack2.pop()

        count = 0

        self.head = None

        while self.stack2.top is not None:
            if count == 0:
                self.head = self.stack2.pop()
                self.stack1.push(self.head)
                count += 1
                continue
        
            self.stack1.push(self.stack2.pop())

        return data
    
    # Time: O(1)
    def peek(self):
        return self.head
    

    
    
    
""" Test for Stack implementation
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
"""

queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.peek())



