
# Time: O(N) | Space: O(1)
def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # this will remove all extra spaces in the string
        s = s.split()
        s.reverse()
        
        return " ".join(s)