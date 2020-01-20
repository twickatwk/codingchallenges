
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

print(largestRange([1,11,3,0,15,5,2,4,10,7,12,6]))