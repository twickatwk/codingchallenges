
# Time: O(N^2) | Space: O(N)
def threeSum(self, A):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        A.sort()
        result = []
        combinations = {}
        
        for i in range(len(A)-2):
            
            left = i+1
            right = len(A)-1
            
            if A[i] > 0:
                continue
            
            while left < right:
                total = A[i] + A[left] + A[right]
                
                if total == 0:
                    # check if this combination already exists
                    if (""+str(A[i])+str(A[left])+str(A[right])) not in combinations:
                        combinations[""+str(A[i])+str(A[left])+str(A[right])] = True
                        result.append([A[i], A[left], A[right]])
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
            
        return result