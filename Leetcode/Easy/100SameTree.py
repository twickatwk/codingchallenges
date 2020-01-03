
# Time: O(N) | Space: O(N) - Space can still be reduced
def isSameTree(p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        t1vals = traverseTree(p, [])
        t2vals = traverseTree(q, [])
        # O(N)
        return t1vals == t2vals

# Time: O(N) | Space: O(D) - depends on the depth of the tree
def traverseTree(tree, array):
    
    if tree is None:
        array.append(None)
        return
    
    array.append(tree.val)
    traverseTree(tree.left, array)
    traverseTree(tree.right, array)
    
    return array