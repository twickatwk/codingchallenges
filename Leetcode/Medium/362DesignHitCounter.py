
class HitCounter(object):
    
    # Space: O(N)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        # you just need to maintain a stack
        self.stamps = []
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.stamps.append(timestamp)
        
    # Time: O(N) | Space: O(1)
    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        minTimestamp = timestamp - 300
        counter = 0
        for i in range(len(self.stamps)-1, -1, -1):
            if self.stamps[i] > minTimestamp:
                counter +=1
            else:
                return counter
        
        return counter
