
def searchNegativePositive(arr):
    
    result = []

    """ Approach 1 -  Two linear search solution
    # Search for the 1st negative num right to left
    negativeNumIndex = -1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < 0:
            negativeNumIndex = i
            break
    result.append(negativeNumIndex)

    # Search for the 1st position num from left to right
    positiveNumIndex = -1
    for i in range(len(arr)):
        if arr[i] >= 0:
            positiveNumIndex = i
            break
    result.append(positiveNumIndex)
    print(result)
    """

    # Approach 2 -  Single linear search solution, assuming 0 is considered positive
    positiveExists = False
    for i in range(len(arr)):
        if arr[i] >= 0:
            positiveExists = True
            if i-1 >= 0:
                result.append(i-1)
            else:
                result.append(-1)
            result.append(i)
            break
        if i == len(arr)-1:
            if not positiveExists:
                result.append(i)
                result.append(-1)
        
    print(result)

searchNegativePositive([-10, -4, -1, 1, 5, 9])
# Expected Output: [2, 3]
searchNegativePositive([1, 4, 5])
# Expected Output: [-1, 0]
searchNegativePositive([-10, -4, -1])
# Expected Output: [2, -1]
