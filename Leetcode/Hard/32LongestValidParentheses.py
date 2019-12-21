
# https://leetcode.com/problems/longest-valid-parentheses/

# Hard

# Time: O(N) | Space: O(N)
def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = []
        validParenthesesIndex = []
        max_count = 0
        count = 0
        for i, char in enumerate(s):
            
            if char == "(":
                stack.append(i)
            elif char == ")" and len(stack) != 0:
                validParenthesesIndex.append([stack.pop(), i])
                # count += 2
            elif char == ")" and len(stack) == 0:
                stack = []
                continue
            if i == len(s)-1:
                if count > max_count:
                    max_count = count
        
        if len(validParenthesesIndex) == 0:
            return 0
        if len(validParenthesesIndex) == 1:
            return validParenthesesIndex[0][1] - validParenthesesIndex[0][0] + 1
        
        validParenthesesIndex.sort()
        # print(validParenthesesIndex)
        
        start = validParenthesesIndex[0][0]
        end = validParenthesesIndex[0][1]
        merged = []
        for i in range(1, len(validParenthesesIndex)):
            if end + 1 >= validParenthesesIndex[i][0]:
                if validParenthesesIndex[i][1] > end:
                    end = validParenthesesIndex[i][1]
            else:
                merged.append([start, end])
                start = validParenthesesIndex[i][0]
                end = validParenthesesIndex[i][1]
        
        
        merged.append([start, end])
        
        
        
        max_count = 0
        for validBrackets in merged:
            print(validBrackets)
            lengthOfValidBrackets = validBrackets[1] - validBrackets[0] + 1
            if lengthOfValidBrackets > max_count:
                max_count = lengthOfValidBrackets
        
        
        return max_count