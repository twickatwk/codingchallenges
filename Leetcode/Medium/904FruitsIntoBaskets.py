
# Time: O(N) | Space: O(1)
def totalFruit(tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        
        if len(tree) == 0:
            return 0
        if len(tree) == 1:
            return 1
        
        fruits = {}
        leftIdx = 0
        rightIdx = 1
        fruits[tree[leftIdx]] = 1
        fruits[tree[rightIdx]] = 1
        maxFruits = 2
        count = 2
        
        while rightIdx+1 < len(tree):
            # if the next fruit is the same as the ones you already have in the basket, simply add them into the basket, and move to the next tree
            if tree[rightIdx+1] in fruits:
                    count += 1
                    rightIdx += 1
                    continue
            else:
                # this means that there are already two kinds of fruits in the baskets, and the next fruit is a different one
                
                if len(fruits) == 2:
                    # check if your current fruit count is the largest so far if so, update max fruit count
                    if count > maxFruits:
                        maxFruits = count
                    # restart the basket
                    fruits = {}
                    # shift the left idx to the current rightidx position
                    leftIdx = rightIdx-1
                    
                    # if the left index is the same as the right index or right index + 1 fruit,
                    # this means that it should have at least 3 fruits to start with
                    if tree[leftIdx] == tree[rightIdx] or tree[leftIdx] == tree[rightIdx+1]:
                        count = 1
                        # keep checking for similar fruits towards the left, till there are no more
                        while leftIdx-1 >= 0 and tree[leftIdx-1] == tree[leftIdx]:
                            count += 1
                            leftIdx -= 1
                    # otherwise, the 3 fruits are completely different
                    else:
                        count = 0

                    # increment the right idx position
                    rightIdx += 1
                    # left index will always be 1 lesser than the right index
                    leftIdx = rightIdx-1
                    # add the two new starting point fruits into the basket
                    fruits[tree[rightIdx]] = 1
                    fruits[tree[leftIdx]] = 1
                    count += 2
                else:
                    # this means that there is still only one type of fruit in the basket, so simply add the new fruit in, and continue
                    fruits[tree[rightIdx+1]] = 1
                    rightIdx += 1
                    count += 1
        
        # check again with whats left in the current basket
        if count > maxFruits:
            maxFruits = count
        
        return maxFruits

print(totalFruit([4,1,1,1,3,1,7,5]))
# Expected Output: 5