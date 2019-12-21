
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Time: O(N) | Space: O(1)
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return False
        if head.next is None:
            return False
        
        
        first = head
        second = head.next.next
        
        if second is None:
            return False
        
        while first is not None and second is not None:
            
            if first == second:
                return True
            
            first = first.next
            if second.next is None:
                return False
            second = second.next.next
            

        return False