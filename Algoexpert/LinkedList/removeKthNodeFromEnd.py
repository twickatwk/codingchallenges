
# https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End

# Medium

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Time: O(N) | Space: O(1)
def removeKthNodeFromEnd(head, k):
    # Write your code here.
	
	first = head
	second = head
	
	for i in range(k):
		second = second.next
		
	
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
		
	prevFirst = None
	
	while second is not None:
		second = second.next
		prevFirst = first
		first = first.next
	
	prevFirst.next = first.next

