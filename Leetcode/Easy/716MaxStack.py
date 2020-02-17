
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = []
        
    # Time: O(1)
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not len(self.stack):
            self.maxStack.append(x)
        else:
            currentMax = self.maxStack[-1]
            if currentMax > x:
                self.maxStack.append(currentMax)
            else:
                self.maxStack.append(x)
        
        self.stack.append(x)
        
    # Time: O(1)
    def pop(self):
        """
        :rtype: int
        """
        
        data = self.stack.pop()
        self.maxStack.pop()
        
        return data
        
    # Time: O(1)
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[-1]
        
        return None

    # Time: O(1)
    def peekMax(self):
        """
        :rtype: int
        """
        return self.maxStack[-1]
        
    # Time: O(N)
    def popMax(self):
        """
        :rtype: int
        """
        print(self.maxStack)
        pos = None
        data = None
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] == self.maxStack[-1]:
                pos = i
                data = self.stack.pop(i)
                self.maxStack.pop(i)
                break
                
        # reset the maxStack
        for i in range(pos, len(self.maxStack)):
            if i == 0:
                self.maxStack[i] = self.stack[i]
                continue
            if self.maxStack[i-1] < self.stack[i]:
                self.maxStack[i] = self.stack[i]
            else:
                self.maxStack[i] = self.maxStack[i-1]
        
        return data