
# Time: O(N) | Space: O(N)
def containsDuplicate(nums):

    dictNums = {}

    for num in nums:
        if num in dictNums:
            return True
        dictNums[num] = True

    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
