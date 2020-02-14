
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

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

secondHead = Node(1)
secondHead.next = Node(2)
secondHead.next.next = Node(3)
secondHead.next.next.next = Node(4)

thirdHead = head.next = Node(2)

print(intersection(head, thirdHead))
