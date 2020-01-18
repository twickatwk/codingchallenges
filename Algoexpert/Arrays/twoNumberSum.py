
# Time: O(N) | Space: O(N)
def twoNumbererSum(array, targetSum):

    dictNums = {}

    for num in array:
        residual = targetSum - num
        if residual in dictNums:
            return [num, residual]
        
        dictNums[num] = True
    
    return []

# Expected Output: [-1, 11]
print(twoNumbererSum([3,5,-4,8,11,1,-1,6], 10))