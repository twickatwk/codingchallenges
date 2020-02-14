
class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        # last is used when new item is added into the queue
        self.last = None
    
    # Time: O(1)
    def enqueue(self, item):

        newNode = QueueNode(item)

        # if there is a last element, enqueue the new node behind it
        if self.last is not None:
            self.last.next = newNode
        self.last = newNode

        # if there is nothing at the top, set the first = last
        if self.first is None:
            self.first = self.last
    
    # Time: O(1)
    def dequeue(self):

        if self.first is None:
            return None
        
        data = self.first.data
        # take the first element out, and set it to the next element
        self.first = self.first.next
        # if there are no more elements, set last to be None
        if self.first is None:
            self.last = None
        
        return data
    
    # Time: O(1)
    def peel(self):
        return self.first
    
    # Time: O(1)
    def isEmpty(self):
        return first is None
        
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())


    

    
