
# Time: O(N) | Space: O(N)
def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        total = 0
        
        total = self.rangeSumBSTHelper(root, L, R, total)
        
        return total
def rangeSumBSTHelper(self, root, L, R, total):
    
    if root is None:
        return total
    
    if root.val >= L and root.val <= R:
        total += root.val
    
    total = self.rangeSumBSTHelper(root.left, L, R, total)
    
    total = self.rangeSumBSTHelper(root.right, L, R, total)
    
    return total