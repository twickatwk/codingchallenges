# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Time: O(N) | Space: O(1)
def deleteNodeFromLinkedList(head, data):

    # if there data that you're deleting is at the head, simply move the head
    if head.data == data:
        return head.next

    node = head

    while node.next is not None:
        if node.next.data == data:
            node.next = node.next.next
            return head # the head node doesnt change, only the reference of the nodes
    
    return head

def printNodesValues(head):
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    print(result)

A = Node(5)
A.next = Node(7)
A.next.next = Node(10)
# Expect: [5, 7, 10]
printNodesValues(A)
A = deleteNodeFromLinkedList(A, 7)
# Expect: [5, 10]
printNodesValues(A)