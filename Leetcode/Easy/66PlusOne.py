
# Time:O(N) | Space:O(1)
def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(digits)-1, -1, -1):
            # if adding one is less than 10, then there is no need to carry forward the value of 1
            if digits[i] + 1 < 10:
                digits[i] += 1
                break
            elif digits[i] + 1 and i == 0:
                digits[i] = 0
                digits.insert(0, 1)
            else:
                digits[i] = 0
        
        return digits