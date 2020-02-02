
class BST:
    # initialize a BST node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    # Average Time:O(Log N) | Worst Time: O(N) | Space: O(1)
    def insert(self, value):
       
        currentNode = self

        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                else:
                    currentNode = currentNode.right

        return self
    
    # Average Time: O(Log N) | Worst Time: O(N) | Space: O(1)
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True

        return False

    # Average Time: O(Log N) | Worst Time: O(N) | Space: O(1)
    def remove(self, value, parentNode=None):
        
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # if there are both branches, you will need to remove the min value in the right branch
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                # if deletion is at the root node where it has only 1 or 0 branches
                if parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break

        return self

    def getMinValue(self):
        node = self
        while node.left is not None:
            node = node.left

        return node.value


