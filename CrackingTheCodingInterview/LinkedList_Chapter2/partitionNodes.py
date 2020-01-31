class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# This approach builds out two separate partitions based on the partition's value
# Time: O(N) | Space: O(1)
def partitionNodes(head, partition):

    leftStart = head
    rightStart = None
    leftEnd = head
    rightEnd = None

    p1 = head.next

    while p1 is not None:

        if p1.data < partition:
            leftEnd.next = p1
            leftEnd = leftEnd.next
        else:
            if rightStart is None:
                rightStart = p1
                rightEnd = p1
            else:
                rightEnd.next = p1
                rightEnd = rightEnd.next

        p1 = p1.next
    #print(leftEnd.data)
    #print(rightStart.data)
    #print(rightEnd.data)
    leftEnd.next = rightStart
    if rightEnd is not None:
        rightEnd.next = None

    return leftStart

def printNodes(head):
    while head is not None:
        print(head.data)
        head = head.next

head = Node(3)
head.next = Node(5)
head.next.next = Node(8)
head.next.next.next = Node(5)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(1)

start = partitionNodes(head,11)
printNodes(start)




