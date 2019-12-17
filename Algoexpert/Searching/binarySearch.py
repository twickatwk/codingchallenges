

# Time: O(Log N) | Space: O(1)
def binarySearch(array, target):
    
    lower = 0
    upper = len(array)-1
    
    while lower < upper:
        mid = (lower+upper)//2
        if target < array[mid]:
            upper = mid-1
            continue
        if target > array[mid]:
            lower = mid+1
            continue
        if target == array[mid]:
            return mid
    
    if array[lower] == target:
        return lower
    if array[upper] == target:
        return upper
    
    return -1

print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))