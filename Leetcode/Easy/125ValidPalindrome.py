
# Time: O(N) | Space: O(N)
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    
    # build out the string with only alphanumeric characters
    
    # 97 to 122, 48 to 57
    
    s = s.lower()
    
    finalString = []
    for c in s:
        
        if (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57):
            finalString.append(c)
    
    # perform palindrome check
    
    finalString = "".join(finalString)
    
    comparison = len(finalString)//2
    
    left = 0
    right = len(finalString)-1
    
    for i in range(comparison):
        if finalString[left] != finalString[right]:
            return False
        left += 1
        right -= 1
    
    return True