# https://leetcode.com/problems/moving-average-from-data-stream/
# Topics: Design, Queue

import collections
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.values = collections.deque([])
        self.sum = 0
        
    # Time: O(1) | Space: O(N)
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.values) < self.size:
            self.values.append(float(val))
            self.sum += float(val)
            # O(1)
            return self.sum / len(self.values)
        elif len(self.values) == self.size:
            # O(1)
            self.sum -= self.values.popleft()
            # O(1)
            self.values.append(float(val))
            self.sum += float(val)
            return self.sum / len(self.values)