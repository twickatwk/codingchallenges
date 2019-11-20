"""
Min Max Stack Construction

Write a Min Max Stack class. The  class should support pushing and popping values
on and off the stack, peeking at values at the top of the stack, and getting both
the minimum and the maximum values in the stack. All class methods, when considered
independently, should run in constant time and with constant space.
"""

class MinMaxStack:
	def __init__(self):
		self.minValue = []
		self.maxValue = []
		self.stack = []
	
    def peek(self):
        # Write your code here.
		if len(self.stack) > 0:
			return self.stack[-1]
		return None

    def pop(self):
        # Write your code here.
		self.maxValue.pop()
		self.minValue.pop()
		return self.stack.pop()
        pass

    def push(self, number):
        # Write your code here.
		if len(self.minValue) == 0:
			self.minValue.append(number)
		else:
			if number < self.minValue[-1]:
				self.minValue.append(number)
			else:
				self.minValue.append(self.minValue[-1])
		if len(self.maxValue) == 0:
			self.maxValue.append(number)
		else:
			if number > self.maxValue[-1]:
				self.maxValue.append(number)
			else:
				self.maxValue.append(self.maxValue[-1])
			
		self.stack.append(number)

    def getMin(self):
        # Write your code here.
		return self.minValue[-1]

    def getMax(self):
        # Write your code here.
		return self.maxValue[-1]