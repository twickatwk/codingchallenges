

# There are three types of edits that can be performed on strings: insert a character, remove a character, 
# replace a character. Given two strings, write a function tock check if they are one edit (or zero edits) away

# Time: O(N) | Space: O(N)
def oneAway(a, b):
    
    # If the difference in the len is more than 2, the it is imposisble to be 1 edit away
    if abs(len(a) - len(b)) > 2:
        return False
    
    # Tracks the number of modification needed
    modificationCount = 0

    # Tracks the number of characters in the first string, a
    dict_chars = {}

    for char in a:
        if char in dict_chars:
            dict_chars += 1
        else:
            dict_chars[char] = 1
    
    for char in b:
        # The character doesnt exists
        if char not in dict_chars:
            modificationCount += 1
        else:
            dict_chars[char] -= 1
            if dict_chars[char] == -1:
                modificationCount += 1
    
    if modificationCount > 1:
        return False
    
    return True

print(oneAway('bale', 'pale'))

        