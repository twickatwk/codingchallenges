

# Average Case: O(N) | Space: O(1)
def searchBST(tree, val):
    
    while root is not None:
        if root.val == val:
            return True
        elif val < root.val:
            root = root.left
        else:
            root = root.right

    return None
