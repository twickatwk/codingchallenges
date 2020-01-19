
# Time: O(N^2) | Space: O(N)
def threeNumberSum(array, targetSum):
    # Write your code here.
	
	result = []
	array.sort()
	for i in range(len(array) - 2):
		currentNum = array[i]
		leftIdx = i + 1
		rightIdx = len(array)-1
		while(leftIdx < rightIdx):
			currentSum = currentNum + array[leftIdx] + array[rightIdx]
			if targetSum > currentSum:
				leftIdx += 1
			elif targetSum < currentSum:
				rightIdx -= 1
			else:
				result.append([currentNum, array[leftIdx], array[rightIdx]])
				leftIdx += 1
				rightIdx -= 1
	return result

# Expected Output: [[-8,2,6],[-8,3,5],[-6,1,5]]
print(threeNumberSum([12,3,1,2,-6,5,-8,6], 0))