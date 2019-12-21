
# Given two strings , write a method to determine whether one if a permutation of another

# Time: O(N Log N) - sorting | Space: O(N)
def checkPermutation(a, b):

    if len(a) != len(b):
        return False

    arrA = list(a).sort()
    arrB = list(b).sort()

    return arrA == arrB

# Time: O(N) | Space: O(N)
def checkPermutation2(a, b):

    if len(a) != len(b):
        return False

    dict_chars = {}

    for char in a:
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1

    for char in b:
        if char not in dict_chars:
            return False
        else:
            dict_chars[char] -= 1
            if dict_chars[char] == -1:
                return False
    
    return True
    

print(checkPermutation2('abca', 'cbaba'))