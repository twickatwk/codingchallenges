
# Given a string, write a function to check if it is a permutation of a palindrome.

# Time: O(N) | Space: O(N)
def checkPalindromePermutation(string):
    string = string.lower()

    dict_chars = {}

    for char in string:
        if char == " ":
            continue
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1

    oddCount = 0

    for char in dict_chars:
        if dict_chars[char] % 2 == 0:
            continue
        else:
            oddCount += 1
            if oddCount > 1:
                return False
    
    return True

print(checkPalindromePermutation("Tact Coa"))