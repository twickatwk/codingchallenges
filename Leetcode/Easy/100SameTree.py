
# Iterative Approach: Time: O(N) | Sapce: O(N)
def isSameTree3(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        
        stack1 = [p]
        stack2 = [q]
        
        while len(stack1) > 0:
            node1 = stack1.pop()
            node2 = stack2.pop()
            
            if node1 is None and node2 is None:
                continue
            
            if node1 is None and node2 is not None:
                return False
            
            if node1 is not None and node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            
            stack1.append(node1.right)
            stack1.append(node1.left)
            
            stack2.append(node2.right)
            stack2.append(node2.left)
        
        return True

# Time: O(N) | Space: O(D) - depends on the depth of the recursion but it is still lesser than the approach below
def isSameTree2(p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None or q is None:
            return p == q
        
        if p.val != q.val:
            return False
        
        return isSameTree2(p.left, q.left) and isSameTree2(p.right, q.right)

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