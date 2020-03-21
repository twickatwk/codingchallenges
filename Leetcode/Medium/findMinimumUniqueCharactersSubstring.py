# ShopBack

# Time: O(N)
# this methods counts the number of unique characters in the string
def countUniqueChars(s):
    
    unique = {}

    for char in s:
        if char not in unique:
            unique[char] = True
            continue
        continue
    
    return unique

# Time: O(N + S) | Space: O(N)
def findUniqueCharacterSubstring(s):
    
    lenOfMinimumSubstring = None
    noUniqueChars = len(countUniqueChars(s))
    
    start = 0
    end = 0

    currentVisitedChars = {}
    
    # keep finding substrings if the end index is smaller than the len of the str
    while end < len(s):

        if s[end] in currentVisitedChars:
            currentVisitedChars[s[end]] += 1
        else:
            currentVisitedChars[s[end]] = 1

        if len(currentVisitedChars) == noUniqueChars:
            startIdx, endIdx = minimiseChars(start, end, s, currentVisitedChars)
            lenOfMinimisedString = endIdx - startIdx + 1
            if lenOfMinimumSubstring is None:
                lenOfMinimumSubstring = lenOfMinimisedString
            else:
                if lenOfMinimisedString < lenOfMinimumSubstring:
                    lenOfMinimumSubstring = lenOfMinimisedString
            start = end + 1
            if start >= len(s):
                break
            end = start
            currentVisitedChars = {}
            continue
            
        end += 1
        

    return lenOfMinimumSubstring


# Time: O(N)
# this method reduces the found substring to have the minimum unique chars
def minimiseChars(start, end, s, currentUniqueChars):
    
    while start != end:
        if s[start] in currentUniqueChars:
            currentUniqueChars[s[start]] -= 1
            if currentUniqueChars[s[start]] < 1:
                break
            else:
                start += 1
    
    return start, end

print(findUniqueCharacterSubstring("dabbcadbc"))
