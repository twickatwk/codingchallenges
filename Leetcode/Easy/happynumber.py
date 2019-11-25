"""
https://leetcode.com/problems/happy-number/
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number 
equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.
"""

# Time: O(dn) | Space: O(n) - Might need to revise as a Floyd Cycle Detection algorithm 
def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        total = 0
        prevTotalCalculations = {}
        numbers = str(n)
        
        while total != 1:
            total = 0
            for num in numbers:
                total += int(pow(int(num),2))
            if total == 1:
                return True
            # this detects endless cycles (sums that you have already computed)
            if total in prevTotalCalculations:
                return False
            else:
                prevTotalCalculations[total] = True
            numbers = str(total)
            
        return False