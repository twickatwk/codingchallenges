def getPermutations(array):
    # Write your code here.
	permutations = []
	getPermutationsHelper(array, [], permutations)
	return permutations

# Time:O(N!.N^2) | Space: O(N!.N)
def getPermutationsHelper(array, currentPermutation, permutations):
	if not len(array) and len(currentPermutation):
		permutations.append(currentPermutation)
	else:
		for i in range(len(array)):
			newArray = array[:i] + array[i+1:]
			newPermutation = currentPermutation + [array[i]]
			getPermutationsHelper(newArray, newPermutation, permutations)
