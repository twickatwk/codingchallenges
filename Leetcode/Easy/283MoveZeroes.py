# Time: O(N) | Space: O(1) - in-place
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    start = 0
    end = None
    
    while start < len(nums)-1:
        while nums[start] != 0:
            start += 1
            if start == len(nums) - 1:
                return nums
            
        end = start + 1

        while nums[end] == 0:
            end += 1
            if end == len(nums):
                return nums
            
        nums[start], nums[end] = nums[end], nums[start]
        
        
        start += 1
    
    return nums