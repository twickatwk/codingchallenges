# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: O(n) | Space: O(n)
def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    l3 = None
    start = None
    
    while l1 is not None and l2 is not None:
        if l3 is None:
            if l1.val <= l2.val:
                l3 = ListNode(l1.val)
                start = l3
                l1 = l1.next
            else:
                l3 = ListNode(l2.val)
                start = l3
                l2 = l2.next
            continue
        else:
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
                l3 = l3.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
                l3 = l3.next
    
    while l1 is not None:
        l3.next = ListNode(l1.val)
        l3 = l3.next
        l1 = l1.next
    
    while l2 is not None:
        l3.next = ListNode(l2.val)
        l3 = l3.next
        l2 = l2.next
    
    return start