
# Time: O(2^n) | Space: O(N)
# Recursive Approach with no memo
def getNthFib(n):

    if n == 1: return 0
    if n == 2: return 1

    return getNthFib(n-1) + getNthFib(n-2)

# Time: O(N) | Space: O(N)
# Using the iterative approach with memo
def getNthFib2(n):

    if n == 1: return 0
    if n == 2: return 1

    fib = [None] * (n+1)

    fib[1] = 0
    fib[2] = 1

    
    for i in range(3, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n]
    

print(getNthFib2(6))