
"""
Write a function that takes in a Binary Tree and return a list of its branch
sums (ordered from leftmost branch sum to rightmost branch sum). A branch sum
is the sum of all values in a Binary Tree
"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Recursive approach : DFS
# Time: O(n) | Space: O(n)
# Each node is visited exactly once, and the call stack depends on the depth of the branch which defines the space
def branchSums(root, total_value=None, results=None):
    # Write your code here.
	if total_value is None:
		total_value = 0
	if results is None:
		results = []
	
    # If you have reach the end of the branch, add the accumulated sum into the result
	if root.left is None and root.right is None:
		total_value += root.value
		results.append(total_value)
		return results
	
    # Continuously add the sum of the branches
	total_value += root.value
	
    # Continuously traverse the left node if its not empty
	if root.left is not None:
		branchSums(root.left, total_value, results)
    
    # Continously traverse the right node if its not empty
	if root.right is not None:
		branchSums(root.right, total_value, results)
	
	return results


