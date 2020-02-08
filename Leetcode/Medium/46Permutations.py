

# Time: O(N * N!) | Space: O(N * N!) - where N represents the length of the array
def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    permutations = []
    self.permuteHelper(nums, [], permutations)
    return permutations

def permuteHelper(self, nums, currentPermutation, permutations):

# if there is no more value to choose from the array,
# this means that a permutation is completed
if not len(nums):
    permutations.append(currentPermutation)
else:
    # for number in the remaining array, you pick it out
    for i in range(len(nums)):
        # you need to create a new array for every possibility, because list are mutable, 
        # otherwise, you will run out of elements
        newNums = nums[0:i] + nums[i+1:]
        newPerm = currentPermutation + [nums[i]]
        self.permuteHelper(newNums, newPerm, permutations)