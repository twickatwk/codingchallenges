
# https://leetcode.com/problems/one-edit-distance/

# Medium 
# Time: O(N) | Space: O(1)
def isOneEditDistance(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    if len(s) == len(t):
        return editReplace(s, t)
    if len(s) + 1 == len(t):
        return editInsert(s, t)
    if len(s) - 1 == len(t):
        return editInsert(t, s)

    return False
    
def editInsert(s, t):
    
    noOfInsertions = 0
    s_index = 0
    t_index = 0
    
    while s_index < len(s) and t_index < len(t):
        if s[s_index] != t[t_index]:
            t_index += 1
            noOfInsertions += 1
            continue
        if s[s_index] == t[t_index]:
            s_index += 1
            t_index += 1
            
    if noOfInsertions == 0:
        return True
    
    if noOfInsertions == 1:
        return True
    
    return False

def editReplace( s, t):
    noOfReplacement = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            noOfReplacement += 1
    
    if noOfReplacement == 1:
        return True
    return False