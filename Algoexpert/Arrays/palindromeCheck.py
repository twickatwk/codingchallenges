# Write a function that takes a non-empty string and that returns a boolean
# representing whether or not the string is a palindrome

"""
# Using the two pointer approach
# Time: O(n) | Space: O(1)
def isPalindrome(string):
    # Write your code here.
    a_idx = 0
    b_idx = len(string)-1
    while a_idx < b_idx:
        if string[a_idx] != string[b_idx]:
            return False
        a_idx += 1
        b_idx -= 1
    
    return True
"""

# Using the recursion approach
# Time: O(n) | Space: O(n)
def isPalindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1] and isPalindrome(string[1:-1]):
        return True
    else:
        return False


