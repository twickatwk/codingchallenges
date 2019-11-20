"""
Min Max Stack Construction

Write a Min Max Stack class. The  class should support pushing and popping values
on and off the stack, peeking at values at the top of the stack, and getting both
the minimum and the maximum values in the stack. All class methods, when considered
independently, should run in constant time and with constant space.
"""

class MinMaxStack:
	def __init__(self):
		self.minMaxStack = []
		self.stack = []
	
    def peek(self):
        # Write your code here.
		if len(self.stack) > 0:
			return self.stack[-1]
		return None

    def pop(self):
        # Write your code here.
		self.minMaxStack.pop()
		return self.stack.pop()
        pass

    def push(self, number):
        # Write your code here.
		newMinMax = {"min":number, "max":number}
		if self.minMaxStack:
			oldMinMax = self.minMaxStack[-1]
			newMinMax["min"] = min(oldMinMax["min"], number)
			newMinMax["max"] = max(oldMinMax["max"], number)
		
		self.minMaxStack.append(newMinMax)
		self.stack.append(number)

    def getMin(self):
        # Write your code here.
		return self.minMaxStack[-1]["min"]

    def getMax(self):
        # Write your code here.
		return self.minMaxStack[-1]["max"]