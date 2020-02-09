
# Time: O(N * 2 ^ N) | Space: O(N * 2 ^ N)
def powerset(array):
	
	subsets = [[]]
	
	for i in range(len(array)):
		currentElement = array[i]
        
		# add new element to all existing subsets, to create new ones
		# and then add them into the list of all subsets
		for j in range(len(subsets)):
			currentSubset = subsets[j]
			subsets.append(currentSubset + [array[i]])
	
	return subsets

print(powerset([1,2,3]))