
# Time: O(N) | Space: (N)
def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dictNums = {}
        
        for num in nums:
            if num in dictNums:
                dictNums[num] += 1
            else:
                dictNums[num] = 1
        
        for key in dictNums:
            if dictNums[key] == 1:
                return key
        
        pass

