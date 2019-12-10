# https://leetcode.com/problems/sort-array-by-parity/

import collections

# Time: O(n) | Space: O(n)
def sortArrayByParity(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    de = collections.deque([])
    # O(n)
    for num in A:
        if num % 2 == 0:
            # O(1)
            de.appendleft(num)
        else:
            de.append(num)
    
    return de

# Time: O(n^2) | Space: O(n)
def sortArrayByParity2(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    result = []
    # O(n)
    for num in A:
        if num % 2 == 0:
            # O(n)
            result.insert(0, num)
        else:
            # O(1)
            result.append(num)
        
    return result
