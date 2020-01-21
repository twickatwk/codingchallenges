
# Time: O(N Log N) - Sorting | Space: O(1)
def largestRange(array):
    # Write your code here.

    array.sort()
    currentValue = array[0]
    maxDistance = 0
    startIndex = 0
    endIndex = 0
    result = [currentValue, currentValue]
    for i in range(1,len(array)):
        if array[i] == currentValue + 1 or array[i] == currentValue:
            endIndex = i
            currentValue = array[i]
            if endIndex - startIndex > maxDistance:
                maxDistance = endIndex - startIndex
                result = [array[startIndex], array[endIndex]]
        else:
            startIndex = i
            endIndex = i
            currentValue = array[i]
    return result

# Time: O(N) - each number in the list is only used/visited once| Space: O(N)
def largestRange2(A):
    
    result = [A[0], A[0]]
    maxDistance = 0

    dictNums = {}

    # Creates a hash table with the numbers in it for reference later on
    for i in range(len(A)):
        if A[i] not in dictNums:
            dictNums[A[i]] = True

    # Goes through each number, and starts building the range
    for i in range(len(A)):
        # Once a number has been used, you toggle it to false
        dictNums[A[i]] = False
        # Initialize the boundaries to the current number
        lowerbound = A[i]
        upperbound = A[i]
        # Find the minimum bound by going to the left, aka decrement from the current num
        while (lowerbound-1 in dictNums and dictNums[lowerbound-1] != False):
            lowerbound -= 1
            dictNums[lowerbound] = False
        # Find the upper bound by going to the right, aka increment from the current num
        while (upperbound+1 in dictNums and dictNums[upperbound+1] != False):
            upperbound += 1
            dictNums[upperbound] = False
        # Check whether the current boundaries has the largest distance
        if upperbound - lowerbound > maxDistance:
            maxDistance = upperbound - lowerbound
            result = [lowerbound, upperbound]

    return result

print(largestRange2([1,11,3,0,15,5,2,4,10,7,12,6]))