# https://leetcode.com/problems/first-unique-character-in-a-string/

# Easy
# Hash Table
# Time: O(N) | Space: O(N)
def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    dict_chars = {}
    uniqueExists = False
    uniqueIndex = len(s)-1
    
    for i, char in enumerate(s):
        if char in dict_chars:
            dict_chars[char] = -1
        else:
            dict_chars[char] = i
    
    # Do a linear search to find the smallest positive index (inclusive of 0)
    for char in dict_chars:
        if dict_chars[char] <= uniqueIndex and dict_chars[char] >= 0:
            uniqueIndex = dict_chars[char]
            uniqueExists = True
    
    # If there are no unique characters, simply return -1
    return uniqueIndex if uniqueExists else -1

print(firstUniqChar("loveleetcode"))