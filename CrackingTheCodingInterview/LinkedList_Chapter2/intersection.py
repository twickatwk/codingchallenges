
# Given two linked list, find whether they have an intersection point, it is based on reference and not value

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Time: O(N) | Space: O(1)
def intersection(node1, node2):

    # find the length of both linked list
    
    l1 = node1
    l2 = node2

    lenL1 = 0
    while l1 is not None:
        lenL1 += 1
        l1 = l1.next
    
    lenL2 = 0
    while l2 is not None:
        lenL2 += 1
        l2 = l2.next
    
    difference = abs(lenL1 - lenL2)
    # if the second linked list is longer, swap them, so the second node will always be the longer linked list
    if lenL2 < lenL1:
        node1, node2 = node2, node1
    
    

    # swift the longer linked list by the difference in length
    for i in range(difference):
        node2 = node2.next
    
    # now that they are aligned in terms of length, simply go through them one step at a time
    while node2 is not None:
        if node1 == node2:
            return True
        node1 = node1.next
        node2 = node2.next

    return False

# Solution from book
# Time: O(N) | Space: O(1)
def intersection2(node1, node2):

    if node1 is None or node2 is None:
        return None
    
    # get the tail node in the linked list and their sizes
    tail1, size1 = getTailAndSize(node1)
    tail2, size2 = getTailAndSize(node2)

    # linked list that intersects should have the same ending node
    if tail1 != tail2:
        return None
    
    shorter = node1
    longer = node2

    if size1 > size2:
        shorter, longer = longer, shorter
    
    # advance the pointer for the longer linked list
    longer = getKthNode(longer, abs(size1-size2))

    # move both pointers until you have a collision
    while node1 != node2 and (node1 is not None and node2 is not None):
        node1 = node1.next
        node2 = node2.next

    # return either one of the linked list works for the intersection point
    return node1

# this method returns the tail of the linked list and its size
# Time: O(N) | Space: O(1)
def getTailAndSize(head):

    size = 1

    while head.next is not None:
        size += 1
        head = head.next
    
    return head, size

# this method returns the head after shiftiung the difference in length of the two linked lists
def getKthNode(head, difference):

    for i in range(difference):
        head = head.next
    
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

secondHead = Node(1)
secondHead.next = Node(2)
secondHead.next.next = Node(3)
secondHead.next.next.next = Node(4)

thirdHead = head.next.next

print(intersection2(head, thirdHead))
