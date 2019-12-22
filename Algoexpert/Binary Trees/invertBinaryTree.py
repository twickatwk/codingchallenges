
# Medium

# Recursive Approach - Time: O(N) | Space: O(N)
def invertBinaryTree(tree):
    # Write your code here.
	
    # When you have reached the left node, there is no need to swap the children nodes
    if tree.left is None and tree.right is None:
        return

    # Perform the swap of the child nodes
    tree.left, tree.right = tree.right, tree.left

    # If a left child still exists, do the same actions, send the 
    # left child and swap the left child's children nodes as well
    if tree.left is not None:
        invertBinaryTree(tree.left)
    # Do the same thing for the right child as well
    if tree.right is not None:
        invertBinaryTree(tree.right)

    return

# Iterative Approach - Time: O(N) | Space: O(N):
def invertBinaryTree2(tree):
    queue = [tree]
    # BFS - uses a queue - FIFO
    while len(queue):
        currentNode = queue.pop(0)
        if currentNode is None:
            continue
        swapNodes(currentNode)
        queue.append(currentNode.left)
        queue.append(currentNode.right)

# This helper method swaps the left and right child nodes
def swapNodes(tree):
	tree.left, tree.right = tree.right, tree.left