
# Time: O(N Log N) - because of the sorting | Space: O(1)
def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        
        return s == t

# Time: O(N) | Space: O(N)
def isAnagram2(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        visitedLetters = {}
        
        for c in s:
            if c in visitedLetters:
                visitedLetters[c] += 1
            else:
                visitedLetters[c] = 1
        
        for c in t:
            if c in visitedLetters:
                visitedLetters[c] -= 1
                if visitedLetters[c] < 0:
                    return False
            else:
                return False
        
        return True