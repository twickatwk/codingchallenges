

# There are three types of edits that can be performed on strings: insert a character, remove a character, 
# replace a character. Given two strings, write a function tock check if they are one edit (or zero edits) away

# Time: O(N) | Space: O(1)
def oneAway(a, b):

    # If both strings are equal, only replace is needed
    if len(a) == len(b):
        return editReplace(a, b)
    # If string a is smaller than string b, which means you need to insert
    if len(a) + 1 == len(b):
        return editInsert(a, b)
    # If string a is larger than string b, which means you need to remove, 
    # but you can switch the strings since remove is the inverse of remove function
    if len(a) - 1 == len(b):
        return editInsert(b, a)

    return False

def editInsert(a, b):
    
    a_idx = 0
    b_idx = 0
    while a_idx < len(a) and b_idx < len(b):
        # Both characters are the same, nothing to insert, increment both pointers
        if a[a_idx] == b[b_idx]:
            a_idx += 1
            b_idx += 1
            continue
        if a[a_idx] != b[b_idx]:
            b_idx += 1
        # if you have replace more than 2 characters, return False
        if b_idx > a_idx + 1:
            return False
    
    return True


def editReplace(a, b):
    noOfReplacement = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            noOfReplacement += 1
    
    if noOfReplacement > 1:
        return False
    
    return True
        


print(oneAway('palr', 'pale'))