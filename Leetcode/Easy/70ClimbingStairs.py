
# Time: O(N) | Space: O(1)
def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        ways = [None] * (n+1)
        ways[1] = 1
        ways[2] = 2
        
        for i in range(3, n+1):
            ways[i] = ways[i-1] + ways[i-2]
            
        return ways[n]

print(climbStairs(3))