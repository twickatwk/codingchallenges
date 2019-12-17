
# https://www.algoexpert.io/questions/Pattern%20Matcher

# Time: O(N^2 + M) | Space: O(N + M) - N is the length of the main string, M is the length of the substring
def patternMatcher(pattern, string):
    # Write your code here.

    # Standardize the pattern by making it start with "x"
    pattern = getNewPattern(pattern)

    # obtain the count for "x" and "y" which will be used to determine the length of x/y, as well as the first occurrence of y
    dict_count, firstY = getCountAndFirstY(pattern)
    
    # Logic for patterns with "x" and "y"
    if firstY is not None:
        # Start the length of "x' as 1 and interate upwards"
        len_of_x = 1
        # Len of Y can be determine by the len of string, number of Xs and the len of X
        len_of_y = int((len(string) - dict_count["x"] * len_of_x) / dict_count["y"])
        
        # First occurrent of Y depends on the firstY position * the length of the current "x" pattern
        y_idx = firstY * len_of_x

        # Keep selecting different possible patterns till len of "y" is 0, which means all patterns have been exhasted
        while len_of_y >= 1:
            newPattern = pattern.copy()
            for i in range(len(pattern)):
                if newPattern[i] == 'x':
                    # Copy the representation of x into the pattern array
                    newPattern[i] = string[0:0+len_of_x]
                else:
                    # Copy the representation of y into the pattern array
                    newPattern[i] = string[y_idx:y_idx+len_of_y]
            # Check whether the substituition is equal to the actual string, otherwise, build a new pattern
            if "".join(newPattern) == string:
                return [string[0:len_of_x], string[y_idx:y_idx+len_of_y]]
            else:
                # Build a new pattern by incrementing x
                len_of_x += 1
                # Redetermine len and index of "y" using the new len of "x"
                len_of_y = int((len(string) - dict_count["x"] * len_of_x) / dict_count["y"])
                y_idx = firstY * len_of_x
        
        return []
    # Logic for only a single "x" or "y" pattern
    else:
        if len(string) % dict_count["x"] != 0:
            return []
        len_of_x = len(string) // dict_count["x"]
        
        for i in range(len(pattern)):
            pattern[i] = string[0:len_of_x]
        
        if "".join(pattern) != string:
            return []
        else:
            return ["", string[0:len_of_x]]





def getCountAndFirstY(arr):
    dict_count = {}
    firstY = None
    for i, value in enumerate(arr):
        if value not in dict_count:
            if value == 'y':
                firstY = i
            dict_count[value] = 1
        else:
            dict_count[value] += 1
    
    return dict_count, firstY


# Standardize the pattern to start with "x"
def getNewPattern(pattern):
    if pattern[0] == "x":
        return list(pattern)
    
    result = ""
    
    for char in pattern:
        if char == 'y':
            result += "x"
        else:
            result += "y"
    return list(result)


print(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"))