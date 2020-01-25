# Iterative Approach
# Average Time: O(Log N) | Worst Time: O(N) | Space: O(1)
def findClosestValueInBst(tree, target):
    # Write your code here.

    if tree.left is None and tree.right is None:
        return tree.value

    result = tree.value
    minDifference = abs(target-tree.value)

    while tree is not None:
        
        difference = abs(target-tree.value)
        
        if difference == 0:
            return tree.value
        
        if difference < minDifference:
            minDifference = difference
            result = tree.value
        
        if tree.value < target:
            tree = tree.right
        else:
            tree = tree.left

    return result

# Recursive Approach
# Average Time: O(Log N) | Worst Time: O(N) | Space: O(D) - Call stack
def findClosestValueInBst2(tree, target):
    # Write your code here.
	
    result, minDifference = traverseTree(tree, target, result=None, minDifference=None)

    return result

def traverseTree(tree, target, result, minDifference):
	
    if tree is None:
        return result, minDifference

    difference = abs(target - tree.value)

    if minDifference is None:
        result = tree.value
        minDifference = difference
    else:
        if difference < minDifference:
            minDifference = difference
            result = tree.value

    if tree.value < target:
        result, minDifference = traverseTree(tree.right, target, result, minDifference)
    if tree.value > target:
        result, minDifference = traverseTree(tree.left, target, result, minDifference)

    return result, minDifference

