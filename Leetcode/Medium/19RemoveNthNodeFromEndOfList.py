# Node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Iterative Approach: Using 3 pointers
# Time: O(N) | Space: O(1)
def removeNthNodeFromEndOfList(head, n):
    p1 = head
    p2 = head

    for i in range(n):
        p2 = p2.next
    
    p3 = None

    while p2 is not None:
        p3 = p1
        p1 = p1.next
        p2 = p2.next

    if p3 is None:
        return head.next
    
    p3.next = p1.next

    return head

def printNodes(head):

    while head is not None:
        print(head.data)
        head = head.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4) 
head.next.next.next.next = Node(5)

head = removeNthNodeFromEndOfList(head, 5)

printNodes(head)
