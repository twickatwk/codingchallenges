
import collections

class TreeNode:
    def __init__s(self, data):
        self.val = data
        self.left = None
        self.right = None

# Time: O(N) - visits each node exactly once using a queue | Space: O(N) - stores each node exactly once
def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    
    queue = collections.deque([root]) 
    levels = []
    level = 0
    
    if root is None:
        return levels
    
    while len(queue):
        levels.append([])
        
        # number of levels in the current level
        levelLength = len(queue)
        
        for i in range(levelLength):
            node = queue.popleft()
            # fill the current level
            levels[level].append(node.val)
            
            # add the child nodes of the current level
            # in the queue for the next level
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
        # go to the next level
        level += 1
        
        
    return levels