
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

head = Node('a')
head.next = Node('b')
head.next.next = Node('c')
head.next.next.next = Node('d')

# Expected: 'c'
returnKthFromLast(head, 2)
