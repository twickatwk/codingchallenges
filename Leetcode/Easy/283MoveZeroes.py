# Time: O(N) | Space: O(1) - in-place
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    start = 0
    end = start
    
    while start < len(nums):
        # keep finding till you find the first 0 for start
        while nums[start] != 0:
            start += 1
            # if start reaches the end of the array, simply stop, and return
            if start == len(nums):
                return nums
        end = start
        while nums[end] == 0:
            end += 1
            # if end reaches the end of array, simply stop, and return
            if end == len(nums):
                return nums
            
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
          
    return nums