
# https://www.algoexpert.io/questions/Search%20In%20Sorted%20Matrix

# Time: O(M+N) | Space: O(1)
def searchInSortedMatrix(matrix, target):
    # Write your code here.
	
	row = 0
	col = 0
	max_col = len(matrix[0])
	
	while row < len(matrix):
		col = 0
		if matrix[row][col] > target:
			break
		while col < max_col:
			if matrix[row][col] == target:
				return [row, col]
			if col + 1 < max_col and matrix[row][col+1] > target:
				max_col = col+1
				break
			else:
				col += 1
		row += 1
	
	return [-1, -1]

print(searchInSortedMatrix([[1, 4, 7, 12, 15, 1000], [2, 5, 19, 31, 32, 1001]], 31))