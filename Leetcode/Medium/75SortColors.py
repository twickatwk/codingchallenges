# this algorithm solves in two passes, it is not the most efficient
# Time: O(N) | Space:O(1)
def sortColors(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # this stores the number of frequency of the different colors
        colors = [0] * 3
        
        # count the number of colors in the array
        for num in nums:
            colors[num] += 1
        
        color = 0
        index = 0
        
        # if any of the colors still have value left, you will continue
        while colors[0] != 0 or colors[1] != 0 or colors[2] != 0:
            # start will the first colour, and once its empty, you move to the next color
            if colors[color] == 0:
                color += 1
                continue
            # replace the current index of the original array with the current color
            nums[index] = color
            # then increment the index of the original array
            index += 1
            # then decrement the count for the current color
            colors[color] -= 1
        
        return nums