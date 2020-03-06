
# Time: O(N) | Space: O(1)
def findMinimumReverse(A):

    startingValue = 1

    noOfChanges = 0

    for num in A:
        if num == startingValue:
            startingValue = toggleValue(startingValue)
            continue
        else:
            noOfChanges += 1
            startingValue = toggleValue(startingValue)

    startingValue = 0
    noOfChanges2 = 0

    for num in A:
        if num == startingValue:
            startingValue = toggleValue(startingValue)
            continue
        else:
            noOfChanges2 += 1
            startingValue = toggleValue(startingValue)
    
    return min(noOfChanges, noOfChanges2)

def toggleValue(num):
    if num == 0:
        return 1
    return 0

print(findMinimumReverse([1,0,1,0,1,1]))

print(findMinimumReverse([1,1,0,1,1]))