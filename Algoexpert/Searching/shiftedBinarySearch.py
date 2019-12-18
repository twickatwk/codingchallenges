

# https://www.algoexpert.io/questions/Shifted%20Binary%20Search

# Time: O(Log N) | Space: O(1)
def shiftedBinarySearch(nums, target):
    # Write your code here.
	
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