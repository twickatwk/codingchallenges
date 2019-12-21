
# https://www.algoexpert.io/questions/Find%20Loop

# Hard

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Approach 2: Using two pointers, and distance between pointer B (point where it meets pointer A) 
# and head node to determine starting of loop
# Time: O(N) | Space: O(1)
def findLoop(head):
    # Write your code here.
    """ Approach 1: Using a dictionary -  Time: O(N) | Space: O(N)
    nodes_visited = {}

    while head is not None:
        if head in nodes_visited:
            break
        else:
            nodes_visited[head] = True
        head = head.next
    """

    # Initialize both pointers at the same starting position
    first = head
    second = head
    # Initialize the variable to track whther they have met to false
    nodesMet = False
    
    # Continue to find the meeting point between pointer A and pointer B
    while not nodesMet:
        # Increment the first pointer at the speed of 1
        first = first.next
        # Increment the second pointer at the speed of 2
        second = second.next.next
        
        # Once the two nodes have met, update the tracker variable to true / break out of loop
        if first == second:
            break
    
    # Distance moved by pointer A = D (distance before loop) + P (distnace after loop)
    # Distance moved by pointer B is twice the distance of pointer A = 2D + 2P
    # Total Distance of the looped linkedlist = D + P + R
    # Another way to write the distance travelled by pointer B = D + P + R + P = D + 2P + R
    # By substuition, D = R, to find D, find the distance where the head (starting from the beginning of the node) and current pointer B meets!

    # Starting counting the distance between the second pointers current position
    while head != second:
        head = head.next
        second = second.next
    
    # This will be starting position of the loop
    return head


