
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Time: O(N) | Space: O(D)
def sumLists(l1, l2):

    # obtain the number representation from the linkedlist
    number1 = int(getNumber(l1))
    number2 = int(getNumber(l2))
    
    # convert the sum of the two numbers into a string
    total = str(number1 + number2)

    # initialize the linked list with the last element in the sum
    result = Node(total[-1])
    start = result

    # go through the sum backwards, build the 
    for i in range(len(total)-2, -1, -1):
        result.next = Node(total[i])
        result = result.next
    
    return start

# Time: O(N) | Space: O(D)
def getNumber(ll):

    if ll.next is None:
        return str(ll.data)
    
    return str(getNumber(ll.next)) + str(ll.data)

def printLinkedList(ll):
    result = ""
    while ll is not None:
        result += ll.data
        ll = ll.next

    return result

ll1 = Node(7)
ll1.next = Node(1)
ll1.next.next = Node(6)

ll2 = Node(5)
ll2.next = Node(9)
ll2.next.next = Node(2)

node = sumLists(ll1, ll2)
# Expected Output: [2 -> 1 -> 9]
print(printLinkedList(node))
