
# Time: O(N Log N) | Space: O(1)
def twoSumLessThanK(self, A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    A.sort()

    l = 0
    r = len(A) - 1

    maxSum = -1

    while l < r:
        
        sumPair = A[l] + A[r]
        
        if sumPair < K:
            if sumPair > maxSum:
                maxSum = sumPair
            l += 1
        else:
            r -= 1

    return maxSum
