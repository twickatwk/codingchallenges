
# Time: O(N) | Space: O(1)
def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True
        
        isIncreasing = None
        prevNum  = A[0]
        for i in range(1, len(A)):
            
            currentNum = A[i]
            
            # if you are still at the first value, you will have to determine whether it's increasing or decreasing based on the second value
            if isIncreasing is None:
                if prevNum < currentNum:
                    isIncreasing = True
                elif prevNum == currentNum:
                    prevNum = currentNum
                    continue
                else:
                    isIncreasing = False
                prevNum = currentNum
                continue
            
            if isIncreasing:
                if prevNum > currentNum:
                    return False
                prevNum = currentNum
                continue
            if not isIncreasing:
                if prevNum < currentNum:
                    return False
                prevNum = currentNum
                continue
        
        return True