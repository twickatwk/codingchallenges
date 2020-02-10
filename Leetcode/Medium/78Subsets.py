# Time: O(N * 2^N) | Space: O(N * 2^N)
def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        subsets = [[]]
        
        for i in range(len(nums)):
            elem = nums[i]
            for j in range(len(subsets)):
                subsets.append(subsets[j] + [elem])
        
        return subsets