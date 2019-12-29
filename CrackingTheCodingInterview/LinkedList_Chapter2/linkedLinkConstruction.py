
# Node Class for LinkedList Implementation
# Very Basic Singly LinkedList
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

# Implement deleteNode function, data on the node is assumed to be unique
# Time: O(N) | Space: O(1)
def deleteNode(head, data):
    # If the node is empty, return
    if head is None:
        return False
    
    nodeToDelete = None
    prevNode = None
    start = head
    # Search through all the nodes to find the node with the "data" value
    while head is not None:
        if head.data == data:
            nodeToDelete = head
            break
        prevNode = head
        head = head.next
    
    # Node is not found
    if nodeToDelete is None:
        return start
    
    # If there is NO nodes BEFORE or AFTER the deleted node - The one and only node
    if prevNode is None and nodeToDelete.next is None:
        nodeToDelete = None
        return None
    
    # If there it NO nodes BEFORE it but there iS nodes AFTER IT - The first node but there are nodes after it
    if prevNode is None and nodeToDelete.next is not None:
        newHead = nodeToDelete.next
        nodeToDelete.next = None
        nodeToDelete = None
        return newHead
    
    # If there is a node BEFORE but NOT AFTER the deleted node - The last node
    if prevNode is not None and nodeToDelete.next is None:
        prevNode.next = None
        nodeToDelete = None
        return start
    
    # If there is a node before and after the deleted node - The middle node
    if prevNode is not None and nodeToDelete.next is not None:
        # Set the previous node's next reference to the deleted node's next reference
        prevNode.next = nodeToDelete.next
        # Deallocate the node
        nodeToDelete.next = None
        nodeToDelete = None

        # Return the head of the Node
        return start
    
    
    

    

ll = Node(1)
ll.appendToTail(3)
ll.appendToTail(5)
ll.appendToTail(7)

ll = deleteNode(ll, 3)
ll = deleteNode(ll, 7)

while ll is not None:
    print(ll.data)
    ll = ll.next



