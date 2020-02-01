

# Time: O(N) - number of nodes in the tree | Space: O(D) - depth of recursion
def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    return self.traverseTree(root, float("-inf"), float("inf"))

def traverseTree(self, root, minValue, maxValue):

    if root is None:
        return True

    if root.val <= minValue or root.val >= maxValue:
        return False

    return self.traverseTree(root.left, minValue, root.val) and self.traverseTree(root.right, root.val, maxValue)
