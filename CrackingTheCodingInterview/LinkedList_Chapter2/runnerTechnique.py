

# Singly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# This method demonstrates the use of two pointers iterating at different speed
# to weave elements together alternating between the starting of the list and the 
# middle of the list
def runnerTechnique(head):
    
    p1 = head
    p2 = head

    # finding the mid point - the starting position of the second part of the linked list to weave
    while p2 is not None:
        p1 = p1.next # moves one step at a time
        p2 = p2.next.next # moves two step at a time

    # now start weaving elements together
    p2 = head
    
    while p1 is not None:
        nextNodeP2 = p2.next
        nextNodeP1 = p1.next
        if nextNodeP1 is None:
            p2.next = p1
            break
        
        p2.next = p1

        p1.next = nextNodeP2
        p2 = nextNodeP2
        p1 = nextNodeP1
    
    return head

def printNodes(head):
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    print(result)

head = Node('a')
head.next = Node('b')
head.next.next = Node('c')
head.next.next.next = Node('d')
head.next.next.next.next = Node('e')
head.next.next.next.next.next = Node('f')

# Original Position of Linked List
printNodes(head)

A = runnerTechnique(head)

# After Position of Linked List
printNodes(A)

