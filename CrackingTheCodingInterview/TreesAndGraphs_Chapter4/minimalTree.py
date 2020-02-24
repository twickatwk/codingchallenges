
# given a sorted (increasing order) array, with unique integer elements, write an algorithm
# to create a binary search tree with minimal height

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createMinimalBST(array):
    return createMinimalBSTHelper(array, 0, len(array)-1)

# Time: O(Log N) | Space: O(D)
def createMinimalBSTHelper(array, start, end):
    if end < start:
        return None

    mid = (start + end) // 2

    node = TreeNode(array[mid])
    node.left = createMinimalBSTHelper(array, start, mid-1)
    node.right = createMinimalBSTHelper(array, mid+1, end)

    return node

def inOrderTraversal(node):

    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data)
    inOrderTraversal(node.right)

arr = [1,2,3,4,5,6,7,8]

node = createMinimalBST(arr)

inOrderTraversal(node)



    


