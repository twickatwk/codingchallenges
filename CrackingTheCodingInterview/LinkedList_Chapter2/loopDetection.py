
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Given a linked list, identify the point where the loop begins

# this method detects whether a loop exists in the linked list
# Time: O(N) | Space: O(1)
def loopDetection(head):

    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return None

def loopDetection2(head):

    slow = head
    fast = head

    # find the meeting point of the two pointers
    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next
         # collision happened
        if slow == fast:
            break
    
    # if the fast pointer can reach the end of the linked list, it means that there is not collision point
    if fast is None or fast.next is None:
        return None
    
    # move the slow pointer to the head, and then shift the slow and fast pointer by 1 step at a time,
    # when they meet again, they will be at the starting point of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    # both of the pointers are now at the start of the loop
    return slow
    



head = Node('A')
head.next = Node('B')
head.next.next = Node('C')
head.next.next.next = Node('D')
head.next.next.next.next = Node('E')
head.next.next.next.next.next = head.next.next

print(loopDetection2(head).data)