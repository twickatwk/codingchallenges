
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: O(N) | Space: O(N)
def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # iterative approach
        newHead = None
        while head is not None:
            n = ListNode(head.val)
            n.next = newHead
            newHead = n
            head = head.next
        
        return newHead
        