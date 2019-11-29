# Stack implementation using Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = self.tail = None

    def push(self, item):
        if self.head is None:
            self.head = self.tail = Node(item)
            return
        if self.head == self.tail:
            temp = Node(item)
            self.head = temp
            temp.next = self.tail
        else:
            temp = Node(item)
            self.tail = self.head
            self.head = temp
            temp.next = self.tail

    def pop(self):
        if self.head is None:
            return
        if self.tail is not None:
            temp = self.head
            self.head = self.tail
            self.tail = self.head.next
            return temp.value
        else:
            temp = self.head
            self.head = self.tail = None
            return temp.value

# Correct Output: 20 10 None 60 50 None
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.push(50)
stack.push(60)
print(stack.pop())
print(stack.pop())
print(stack.pop())
