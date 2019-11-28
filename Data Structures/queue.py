# Queue Implementation using Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def enqueue(self, item):
        temp = Node(item)
        if self.tail is None:
            self.head = self.tail = temp
            return
        else:
            self.tail.next = temp
            self.tail = temp
    def dequeue(self):
        if self.isEmpty():
            return
        else:
            temp = self.head
            self.head = temp.next
            if self.head is None:
                self.tail = None
            return str(temp.value)


# Driver Code 
if __name__== '__main__': 
    q = LinkedList() 
    q.enqueue(10) 
    q.enqueue(20) 
    q.dequeue() 
    q.dequeue() 
    q.enqueue(30) 
    q.enqueue(40) 
    q.enqueue(50) 

    print("Dequeued item is " + q.dequeue()) 
     



