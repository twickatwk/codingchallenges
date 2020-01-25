
# Time: O(M+N) | Space: O(M+N) - Call stack
def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        subTreePath = self.traverseTree(t)
        mainTreePath = self.traverseTree(s)
        print(mainTreePath)
        print(subTreePath)
        if subTreePath in mainTreePath:
            return True
        
        return False
    
def traverseTree(self, node):
    
    if node is None:
        return "end"

    return "|" + str(node.val) + "|" + self.traverseTree(node.left) + "|" + self.traverseTree(node.right)