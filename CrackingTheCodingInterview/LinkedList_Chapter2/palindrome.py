
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

# Approach: Reverse and Compare
# Time: O(N) | Space: O(N)
def isPalindrome2(head):
    reverse = reverseAndClone(head)
    return isEqual(head, reverse)

# Time: O(N) | Space: O(N)
def reverseAndClone(node):
    head = None
    while node is not None:
        # clone the data
        n = Node(node.data)
        # sets the next node to be the head of the new linked list
        n.next = head
        # update the head back to the top of the new linked list
        head = n
        # iterate the next node of the current linked list
        node = node.next
    
    return head

# Time: O(N) | Space: O(1)
def isEqual(one, two):
    # check both linked list, going through them one by one
    while one is not None and two is not None:
        if one.data != two.data:
            return False
        one = one.next
        two = two.next
    
    return True



head = Node(0)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(0)

print(isPalindrome2(head))
