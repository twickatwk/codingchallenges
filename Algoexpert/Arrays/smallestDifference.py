
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

# Approach 2: Uses sorted arrays
# Time: O(N log N) | Space: O(1)
def smallestDifference2(arrayOne, arrayTwo):
    # Write your code here.
	
	arrayOne.sort()
	arrayTwo.sort()
	
	aIdx = 0
	bIdx = 0
	
	minDifference = float("inf")
	result = []
	
	while aIdx < len(arrayOne) and bIdx < len(arrayTwo):
		num1 = arrayOne[aIdx]
		num2 = arrayTwo[bIdx]
		difference = abs(num1 - num2)
        if difference == 0:
            return [num1, num2]
		if difference < minDifference:
			minDifference = difference
			result = [num1, num2]
		if num1 < num2:
			aIdx += 1
		else:
			bIdx += 1
	return result
