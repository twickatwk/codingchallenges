

def sameBsts(arrayOne, arrayTwo):
    
    return traverseTree(arrayOne, arrayTwo)

# Time: O(N^2) | Space: O(N^2)
def traverseTree(A, B):
    if len(A) != len(B):
        return False
    if len(A) == 0 and len(B) == 0:
        return True
    if A[0] != B[0]:
        return False
    
    # retrieve values that are larger or equal to the current node
    largerA = getLargerOrEqual(A, A[0])
    largerB = getLargerOrEqual(B, B[0])
    # retrieve values that are smaller than the current node
    smallerA = getSmaller(A, A[0])
    smallerB = getSmaller(B, B[0])

    return traverseTree(smallerA, smallerB) and traverseTree(largerA, largerB)

# Time: O(N) | Space: O(N)
def getLargerOrEqual(A, value):
    
    result = []
    for i in range(1, len(A)):
        if A[i] >= value:
            result.append(A[i])

    return result

# Time: O(N) | Space: O(N)
def getSmaller(A, value):
    
    result = []
    for i in range(1, len(A)):
        if A[i] < value:
            result.append(A[i])

    return result


print(sameBsts([10,15,8,12,94,81,5,2,11],[10,8,5,15,2,12,11,94,81]))
