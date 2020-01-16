
# Time: O(N) | Space: O(N)
def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        A = [None] * (len(nums)+1)
        
        for num in nums:
            A[num] = 1
        
        for i, num in enumerate(A):
            if num == None:
                return i

print(missingNumber([9,6,4,2,3,5,7,0,1]))