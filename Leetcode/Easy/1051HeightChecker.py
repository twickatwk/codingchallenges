
# Time: O(N log N) | Space: O(N)
def heightChecker(heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        heights_sorted = heights[:]
        
        heights_sorted.sort()
        
        swaps = 0
        
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                swaps += 1
        
        return swaps