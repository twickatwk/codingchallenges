
# https://www.algoexpert.io/questions/Product%20Sum

# Easy

""" Cleaner Solution """
# Time: O(N) - N represents the number of elements | Space: O(D) - depth of the recursion depending on the size of the sub list 
def productSum2(array, multiplier=1):
    total = 0

    for element in array:
        if type(element) is int:
            total += element
        else:
            total += productSum2(element, multiplier+1)
    
    return multiplier * total

def productSum(array):
    # Write your code here
	
	multiplier = 1
	total = 0
	
	for item in array:
		# Multiplier starts from 2 because the first level will not be affect, as if it's an integer, 
		# it will be returned immediately with a multiplier of 1
		total += calculateSumWithinList(item, multiplier+1, 0)
	
	return total

# Time: O(N) | Space: O(D) - depends ont the depth of the array
def calculateSumWithinList(items, multiplier, total):
	
	if type(items) is int:
		# If the item if an integer, simply return it, there is nothing to recurse
		return items
	
	for item in items:
		# Sum will always be initilized to 0 for each depth you go to, with an increment of 1 for its multiplier
		total += calculateSumWithinList(item, multiplier+1, 0)
		
	# After calcuating the total, you have to return the total multplied by its depth
	return multiplier * total


print(productSum2([5,2,[7,-1],3,[6,[-13, 8], 4]]))

print(productSum([5,2,[7,-1],3,[6,[-13, 8], 4]]))

# Expected: 12