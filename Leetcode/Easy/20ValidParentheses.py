
# Time: O(N) | Space: O(N)
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    
    stack = []
    openings = {')': '(', '}': '{', ']': '['}
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        else:
            if not len(stack):
                return False
            validOpening = stack.pop()
            if validOpening != openings[s[i]]:
                return False
    
    if len(stack) != 0:
        return False
    
    return True