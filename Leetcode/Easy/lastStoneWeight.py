

# https://leetcode.com/problems/last-stone-weight/

# Easy
# Recursion


class Solution(object):

    # Time: O(N) | Space: O(N)
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        print(stones)
        result = self.smashStones(stones)
        
        return result
        
    def smashStones(self, stones):
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        
        y = stones[-1]
        print(y)
        x = stones[-2]
        print(x)
        if x == y:
            stones.pop()
            stones.pop()
            return self.smashStones(stones)
            
        else:
            stones.pop()
            stones[-1] = y-x
            stones.sort()
            return self.smashStones(stones)