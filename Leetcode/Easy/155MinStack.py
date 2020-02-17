
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        
    # Time: O(1)
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not len(self.stack):
            self.minStack.append(x)
        else:
            if self.minStack[-1] < x:
                self.minStack.append(self.minStack[-1])
            else:
                self.minStack.append(x)
        self.stack.append(x)
        
    # Time: O(1)
    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0:
            self.stack.pop()
            self.minStack.pop()
        
    # Time: O(1)
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    # Time: O(1)
    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
