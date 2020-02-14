
# a stack can be implemented using a linked list
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None

    # Time: O(1) | Space: O(1)
    def pop(self):
        # if there it no more items in the stack, return None
        if self.top is None:
            return None
        # obtain the item from the top of the linked list
        item = self.top
        # shift the top of the stack to the next element in the linked list
        self.top = self.top.next
        return item
    
    # Time: O(1)
    def push(self, item):
        # create a new node
        node = StackNode(item)
        # set the next node in the stack to the current head of the stack
        node.next = self.top
        # then set the top of the stack to the current newly added item
        self.top = node
    
    # Time: O(1)
    def peek(self):
        return self.top.data
    
    # Time: O(1)
    def isEmpty(self):
        return self.top is None

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop().data)
print(stack.pop().data)
# Expected Output: 3 2


    