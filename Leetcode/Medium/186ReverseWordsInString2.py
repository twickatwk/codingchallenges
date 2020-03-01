

# Time: O(N) - number of words in the array | Space: O(1)
def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(s)-1
        
        # this swaps the letters to the correct reversed position
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
        index = 0
        endIndex = 0
        while endIndex < len(s):
            if s[endIndex] != " ":
                endIndex += 1
                continue
                
            swapLetters(s, index, endIndex-1)
            
            endIndex += 1
            index = endIndex
            
        swapLetters(s, index, endIndex-1)
            
# swaps the letters in the word
def swapLetters(s, start, end):
    
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    
    return s