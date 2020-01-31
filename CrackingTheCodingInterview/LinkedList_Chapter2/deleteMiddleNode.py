class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# This method deletes the middle node, without any given node
# Time: O(N) | Space: O(1)
def deleteMiddleNode(head):
    
    # for odd length linked list, p2.next will reach None
    # for even length linked list, p2 will reach None

    if head is None or head.next is None:
        head = None
        return head

    p1 = head
    p2 = head
    prev = None

    while p2 is not None and p2.next is not None:
        prev = p1
        p1 = p1.next
        p2 = p2.next.next

    prev.next = p1.next

    return head

# This method will remove the any middle node that is given
# Time: O(N) | Space: O(1)
def deleteMiddleNode2(head, nodeToDelete):
    p1 = head
    # basically you go to the node before the node to delete
    while p1.next.data != nodeToDelete.data:
        p1 = p1.next
    # replace the node before's next node to the nodeToDelete's next node
    p1.next = nodeToDelete.next

    return head

# Solution
# Time: O(1) | Space: O(1)
def deleteMiddleNode3(head, nodeToDelete):
    if nodeToDelete is None or nodeToDelete.next is None:
        return head
    
    # take the next node from the nodeToDelete
    nextNode = nodeToDelete.next
    # update the current node (nodeToDelete) to it's next node
    nodeToDelete.data = nextNode.data
    nodeToDelete.next = nextNode.next

    return head


def printNodes(head):
    while head is not None:
        print(head.data)
        head = head.next

head = Node('a')
head.next = Node('b')
head.next.next = Node('c')
nodeToDelete = head.next.next
head.next.next.next = Node('d')
head.next.next.next.next = Node('e')
# head = deleteMiddleNode(head)
head = deleteMiddleNode3(head, nodeToDelete)
printNodes(head)
