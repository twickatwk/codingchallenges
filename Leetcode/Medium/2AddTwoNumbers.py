
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # Time: O(N) | Space: O(N) - depends on the result, which will determine the length of the linked list
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # O(N)
        num1 = self.obtainNumber(l1)
        # O(N)
        num2 = self.obtainNumber(l2)
    
        additionOfNums = str(int(num1) + int(num2))
        
        # O(N)
        result = additionOfNums[::-1]
        
        node = ListNode(result[0])
        head = node
        
        # O(N)
        for i in range(1, len(result)):
            node.next = ListNode(result[i])
            node = node.next
        
        return head
            
    
    def obtainNumber(self, ll):
        
        if ll is None:
            return ""
        
        return "" + self.obtainNumber(ll.next) + str(ll.val)