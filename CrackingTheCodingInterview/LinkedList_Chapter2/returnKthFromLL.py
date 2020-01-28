
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
# Time; O(N) | Space:O(N)
def returnKthFromLast2(head, size, k):

    kthElement = size - k

    for i in range(kthElement):
        head = head.next

    return head.data

head = Node('a')
head.next = Node('b')
head.next.next = Node('c')
head.next.next.next = Node('d')
head.next.next.next.next = Node('e')
# Expected: 'd'
returnKthFromLast(head, 2)
print(returnKthFromLast2(head, 5, 2))
