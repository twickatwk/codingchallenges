
# https://leetcode.com/problems/logger-rate-limiter/

# Easy

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messageStream = {}
        
    # TimeL O(1) | Space: O(N)
    # Uses a dictionary, so insertion and retrieval is constant time, while space depends on the number of items in the dictonary
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.messageStream:
            self.messageStream[message] = timestamp
            return True
        if message in self.messageStream:
            lastExecutedTimeStamp = self.messageStream[message]
            if abs(timestamp - lastExecutedTimeStamp) >= 10:
                self.messageStream[message] = timestamp
                return True
        
        return False





# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)