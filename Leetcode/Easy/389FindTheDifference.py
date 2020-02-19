
# Time: O(N) | Space: O(N)
def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        letters = {}
        
        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        
        for char in t:
            if char not in letters:
                return char
            if char in letters:
                letters[char] -= 1
                if letters[char] < 0:
                    return char
        
        return False