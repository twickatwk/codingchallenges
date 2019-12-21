
# Develop a function that checks whether the string has all unique characters

# Time: O(N) | Space: O(N) uses a dictionary
def isUnique(string):
    dict_characters = {}
    unique = True
    for char in string:
        if char in dict_characters:
            unique = False
        else:
            dict_characters[char] = True
    
    return unique

# Time: O(N Log N) | Space: O(1)
def isUnique2(string):

    arr = list(string)
    # Time: O(Log N)
    arr.sort()

    unique = True

    # Time: O(N)
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            unique = False
    
    return unique

print(isUnique2('abx'))