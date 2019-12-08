import unittest

# https://www.algoexpert.io/questions/Longest%20Palindromic%20Substring
# Write a function that given a string, return its longest palindromic substring

# Aaron's approach using two pointers in a single walkthrough
# Time: O(n^2) | Space: O(1)
def longestPalindromicSubstring(string):
    # Write your code here.
    if len(string) <= 2:
        return string

    start = 0
    end = 0
    difference = end - start
    for i in range(1, len(string)):
        r_index = i
        l_index = r_index - 1
        
        while (l_index >= 0 and r_index < len(string)) and (string[l_index] == string[r_index]):
            l_index -= 1
            r_index += 1
        if (r_index-l_index) > difference:
            difference = r_index-l_index
            start = l_index
            end = r_index
        
        if ((i-1) >= 0 and (i+1) < len(string)) and (string[i-1] == string[i+1]):
            r_index = i+1
            l_index = i-1
        else: 
            continue
        
        while (l_index >= 0 and r_index < len(string)) and (string[l_index] == string[r_index]):
            l_index -= 1
            r_index += 1
        if (r_index-l_index) > difference:
            difference = (r_index-l_index)
            start = l_index
            end = r_index

    return string[start-1:end]







