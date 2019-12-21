

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

print(fib(3))