
# Node Class for LinkedList Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # Time: O(N) | Space: O(1)
    # You go through each element till you reach the last node with not "next" reference and append the new node there
    def appendToTail(self, data):
        node = Node(data)
        while self.next is not None:
            self = self.next
        
        self.next = node

ll = Node(1)
ll.appendToTail(3)
ll.appendToTail(5)
ll.appendToTail(7)

while ll is not None:
    print(ll.data)
    ll = ll.next



