
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# This approach doesnt return the node value
# Time: O(N) | Space:O(N) - depends on the depth of the call stack
def returnKthFromLast(head, k):

    if head is None:
        return 0

    index = returnKthFromLast(head.next, k) + 1
    
    if index == k:
        print(head.data)

    return index

# This approach assumes that the size of the linked list is given
# Time: O(N) | Space:O(N)
def returnKthFromLast2(head, size, k):

    kthElement = size - k

    for i in range(kthElement):
        head = head.next

    return head.data

# This iterative approach uses two pointers without the need of knowing the size of the linked list
# Time: O(N) | Space: O(1) - Most optimal solution
def returnKthFromLast3(head, k):

    p1 = head
    p2 = head
    for i in range(k):
        p2 = p2.next

    while p2 is not None:
        p1 = p1.next
        p2 = p2.next

    return p1.data

head = Node('a')
head.next = Node('b')
head.next.next = Node('c')
head.next.next.next = Node('d')
head.next.next.next.next = Node('e')
# Expected: 'd'
returnKthFromLast(head, 2)
print(returnKthFromLast2(head, 5, 2))
print(returnKthFromLast3(head, 2))
