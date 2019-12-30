
# https://www.algoexpert.io/questions/Product%20Sum

# Easy

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