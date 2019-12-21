# https://leetcode.com/problems/fibonacci-number/

# Easy

# This approach uses recursion but its not optimal yet
# Time: O(2^N) | Space: O(N)
def fib(N):
    """
    :type N: int
    :rtype: int
    """
    
    if N == 1:
        return 1
    if N == 0:
        return 0
    
    return fib(N-1) + fib(N-2)


# This approach is the most optimal, for fib numbers that are previously calculated, you do not recalculate them, by maintaing a memo table
# Time: O(N) - each fib number is only counted exactly once | Space: O(N)
def fib2(N, prevNums=None):
        """
        :type N: int
        :rtype: int
        """
        if prevNums is None:
            prevNums = {}
        
        if N == 1:
            return 1
        if N == 0:
            return 0
        
        if N in prevNums:
            return prevNums[N]
        
        prevNums[N] = fib2(N-1, prevNums) + fib2(N-2, prevNums)
        
        return prevNums[N]

print(fib2(3))