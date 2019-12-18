

# https://leetcode.com/problems/intersection-of-two-linked-lists/

def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        count = 0
        ref = headA
        # Find the len of the first linked list
        while ref is not None:
            count += 1
            ref = ref.next
        lenNodeA = count
        
        count = 0
        ref = headB
        # Find the len of the second linked list
        while ref is not None:
            count += 1
            ref = ref.next
        lenNodeB = count
        
        # Make "headA" the head of the longer linked list
        if lenNodeB > lenNodeA:
            headA, headB = headB, headA
        
        # Get the difference between the two linked list
        diff = abs(lenNodeB-lenNodeA)
        
        # Move the longer linked list ahead by the difference
        for i in range(diff):
            headA = headA.next
            
        # Traverse the two linked list in parallel, since they are starting at the same location
        while headA is not None:
            # If the address of the two linked list is the same, then a intersection has happened
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        # Otherwise return None if no intersection is found
        return None






