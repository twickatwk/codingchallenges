
# Approach 1: Brute Force
# Time: O(N^2) | Space: O(1)
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	
	result = []
	minDifference = float("inf")
	
	for num1 in arrayOne:
		for num2 in arrayTwo:
			difference = abs(num1-num2)
			if difference < minDifference:
				minDifference = difference
				result = [num1, num2]
	return result



