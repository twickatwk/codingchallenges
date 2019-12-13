# https://www.algoexpert.io/questions/Longest%20Substring%20Without%20Duplication

def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest_substring = [0, 1]
    startIndex = 0
    
    for i, char in enumerate(string):
        if char in lastSeen:
            startIndex = max(startIndex, lastSeen[char] + 1)
        if longest_substring[1] - longest_substring[0] < i + 1 - startIndex:
            longest_substring = [startIndex, i+1]
        lastSeen[char] = i
    
    return string[longest_substring[0]:longest_substring[1]]





"""
# Aaron's Approach: Time: O(N) | Space: O(N) - either the length of lastSeen or max_string
def longestSubstringWithoutDuplication(string):
    # Write your code here.
	
	idx = 0
	lastSeen = {}
	max_string = ""
	i = 0
	# Starting point of a new substring
	while (idx < len(string)):
		# Building the new substring
		while (i <= len(string)):
			# if you have reached the end of the string, terminate
			if i == len(string):
				idx = len(string)
				break
			# Check whether you have last seen that character in the string or if the character you have seen is the same
			if string[i] not in lastSeen or lastSeen[string[i]] == i:
				# If its not there, store the position of the character to last seen
				lastSeen[string[i]] = i
				# Check whether the len of the current substring is larger than the current maximum substring
				len_of_substring = (i+1) - idx
				if len_of_substring > len(max_string):
					# Update the new maximum substring
					max_string = string[idx:i+1]
				i += 1
			else:
				# Otherwise, update the new starting point (idx) as the max of the current index
				prev_idx = idx
				idx = max(idx, lastSeen[string[i]] + 1)
				lastSeen[string[i]] = i
				if prev_idx == idx:
					continue
				break
				i = idx
	return max_string
"""