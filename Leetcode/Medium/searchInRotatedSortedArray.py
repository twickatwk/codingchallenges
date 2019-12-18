

# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Time: O(Log N) | Space; O(1)
def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        
        lower = 0
        upper = len(nums) - 1

        while lower+1 < upper:
            mid = (lower+upper)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[lower]:
                if target >= nums[lower] and target < nums[mid]:
                    upper = mid - 1
                else:
                    lower = mid + 1
            else:
                if target > nums[mid] and target <= nums[upper]:
                    lower = mid + 1
                else:
                    upper = mid - 1

        if nums[lower] == target:
            return lower
        if nums[upper] == target:
            return upper

        return -1






