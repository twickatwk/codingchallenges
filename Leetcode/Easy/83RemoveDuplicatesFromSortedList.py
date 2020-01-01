# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Easy
# Linked List

# Time: O(N) | Space: O(1)
def deleteDuplicates(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        p1 = head
        p2 = None
        if p1 is not None:
            p2 = head.next
        
        while p2 is not None:
            while p1.val == p2.val:
                # temp pointer is used to Deallocate the memory
                temp = p2
                p2 = p2.next
                # Deallocate memory (delete previous similar nodes' reference)
                temp.next = None

                if p2 is None:
                    p1.next = None
                    return head
            p1.next = p2
            p1 = p2
            p2 = p1.next
        
        return head