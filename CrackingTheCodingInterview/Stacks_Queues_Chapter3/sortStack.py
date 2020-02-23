
# linked list node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# stack definition
class Stack:
    def __init__(self):
        self.top = None
    
    def peek(self):
        return self.top.data

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
            return
        
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
    
    def pop(self):
        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.next

        return data

    def display(self):
        top = self.top
        while top is not None:
            print(top.data)
            top = top.next

# Time: O(N^2) | Space: O(N)
def sortStack(stack):
    # this is the sorted version of the stack
    r = Stack()
    # only stop when the original stack is empty
    while not stack.isEmpty():
        # remove one item from the original stack
        tmp = stack.pop()
        # if the current item is smaller than the sorted stack, r, then take items out of the sorted stack, and push it into the original stack
        while not r.isEmpty() and r.peek() > tmp:
            stack.push(r.pop())
        # once the current item is larger than the sorted stack's top item, or if the sorted stack is empty,
        # simply add the current item into the sorted stack
        r.push(tmp)
    
    # for ascending stack, copy the sorted stack and replace it into the original stack for display
    while not r.isEmpty():
        stack.push(r.pop())
    
    return stack

stack = Stack()
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(1)
stack.push(7)
stack.push(2)

sortedStack = sortStack(stack)
sortedStack.display()


