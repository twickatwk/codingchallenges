
# Time: O(N) | Space: O(1)
def subarraySort(A):
    # Write your code here.
	
    maxValue = float("-inf")
    minValue = None

    minRange = -1
    maxRange = -1

    for i in range(len(A)):
        if A[i] >= maxValue:
            maxValue = A[i]
        else:
            if minValue is None:
                minRange, minValue = searchMinValue(i, A)
            maxRange = i
    
    return[minRange, maxRange]

def searchMinValue(i, A):
    minRange = -1
    minValue = float("inf")

    for i in range(i, len(A)):
        if A[i] < minValue:
            minValue = A[i]
    
    for i in range(0, i):
        if A[i] > minValue:
            return i, minValue

    return minRange, minValue    


    
# Expected Output: [4, 6]
print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]))