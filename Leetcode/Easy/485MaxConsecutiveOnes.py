
# Time: O(N) | Space: O(1)
def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxStreak = 0
        currentStreak = 0
        for num in nums:
            if num == 1:
                currentStreak += 1
            else:
                if currentStreak > maxStreak:
                    maxStreak = currentStreak
                currentStreak = 0
        
        if currentStreak > maxStreak:
            maxStreak = currentStreak
        
        return maxStreak