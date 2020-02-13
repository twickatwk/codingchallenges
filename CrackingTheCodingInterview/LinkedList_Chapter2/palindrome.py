
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
    
    # keep checking till midpoint pointer goes to the end
    while midpoint is not None:
        # move the pointers at the same speed, but both pointers need to have the same data, otherwise, it is not a palindrome
        if midpoint.data != idxA.data:
            return False
        midpoint = midpoint.next

    return True

head = Node(1)

head.next = Node(2)

print(isPalindrome(head))
