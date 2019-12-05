# Given an array of integers, A, sorted in non-decreasing order, return an
# array of the squares of each number, also in sorted non-decreasing order

# Time: O(n log n) | Space: O(1)
def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(A)):
            A[i] = A[i]*A[i]
        
        # Assuming primitive sort() function does merge sort
        A.sort()
        return A