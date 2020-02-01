



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time: O(N) - the number of nodes in the tree | Space: O(D) - depth of the recursion
def validateBst(tree):
    # Write your code here.
    
    minValue = float("-inf")
    maxValue = float("inf")
    
    return traverseTree(tree, minValue, maxValue)

def traverseTree(tree, minValue, maxValue):
    
    if tree is None:
            return True
    
    if tree.value < minValue or tree.value >= maxValue:
            return False
    
    isLeftValid = traverseTree(tree.left, minValue, tree.value)
    return isLeftValid and traverseTree(tree.right, tree.value, maxValue)
