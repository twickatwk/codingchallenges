# Recursive Approach
# Average Time: O(Log N) | Space: O(D)
def findClosestValueInBst(tree, target):
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

