
# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

# Easy

'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

# Time: O(N) | Space: O(1)
def height(root, leftDepth=None, rightDepth=None):

    if leftDepth is None:
        leftDepth = 0
    if rightDepth is None:
        rightDepth = 0


    if root.left is None and root.right is None:
        return 0
    
    # As long as the left child node is not None, keep traversing, and add 1 for every left traversal
    if root.left is not None:
        leftDepth += height(root.left) + 1
    
    # As long as the right child node is not None, keep traversing, and add 1 for every right traversal
    if root.right is not None:
        rightDepth += height(root.right, rightDepth) + 1
    
    # Once both the left and right possible traverse if done, take the one that is deeper in depth
    return max(leftDepth, rightDepth)