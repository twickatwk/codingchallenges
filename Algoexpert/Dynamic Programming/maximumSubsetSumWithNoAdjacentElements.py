
# Time: O(N) | Space: O(N)
def maxSubsetSumWithNoAdjacentElements(arr):

    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return arr[0]
    
    if len(arr) == 2:
        return max(arr[0], arr[1])

    maxSubsetSum = [arr[0], max(arr[0], arr[1])]

    for i in range(2, len(arr)):
        # the current maximum sum for the current position is:
        # i-1 (maxSubsetSum) position's value vs. i-2 (maxSubsetSum) position + i (arr) position's value
        # at every point in time,  you store the largest position sum, from either maximum value 
        # from your previous position or the current position's value + maximum value from 2 positions away
        maxSubsetSum.append(max(maxSubsetSum[i-1], maxSubsetSum[i-2]+arr[i]))
    
    # the last element of the maxSubsetSum is the largest possible sum of them all fulfilling the non-adjacency rule
    return maxSubsetSum[-1]

print(maxSubsetSumWithNoAdjacentElements([75,105,120,75,90,135]))