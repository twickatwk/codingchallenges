
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Time: O(N) | Space: O(V)
def removeDuplicates(head):
    if head is None:
        return

    node = head
    values = {}

    while node is not None:
        
        if node.data not in values:
            values[node.data] = True
            prevNode = node
            node = node.next
        else:
            prevNode.next = node.next
            node = node.next
    
    return head

def printNodes(head):
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    
    print(result)

A = Node(1)
A.next = Node(1)
A.next.next = Node(2)
A.next.next.next = Node(2)
A.next.next.next.next = Node(2)
A.next.next.next.next.next = Node(3)
A.next.next.next.next.next.next = Node(2)

removeDuplicates(A)

printNodes(A)