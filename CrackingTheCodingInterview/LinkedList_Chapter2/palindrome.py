
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Time: O(N) | Space: O(1)
def isPalindrome(node):
    
    if node.next is None:
        return True
    
    # start two pointers, traveling at different speed in the linked list
    idxA = node
    idxB = node

    while idxB is not None and idxB.next is not None:
        # move at the speed of one
        idxA = idxA.next

        # move at the speed of two aka twice the speed
        idxB = idxB.next.next
    
    isOdd = True
    
    # if idxB is None, means that the linked list is even
    if idxB is None:
        isOdd = False
    
    # obtain mid point from pointer A
    midpoint = idxA

    # reset pointer A back to the beginning
    idxA = node
    
    if isOdd:
        midpoint = midpoint.next
    
    # add the first and second half of the linked list into separate list
    l1 = []
    l2 = []
    while midpoint is not None:
        l1.append(midpoint.data)
        l2.append(idxA.data)
        midpoint = midpoint.next
        idxA = idxA.next

    # compare the l2 with the reverse of l1
    l1.reverse()
    if l1 != l2:
        return False

    return True



head = Node(0)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(0)

print(isPalindrome(head))
