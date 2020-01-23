
# Time: O(N) - Every node is visited exactly once | Space: O(1)
def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    
    helper(root)
    
    return root
    
def helper(root):
    if root is None:
        return
    
    # at the current node, swap the left and right child nodes
    
    root.left, root.right = root.right, root.left
    
    helper(root.left)
    helper(root.right)
