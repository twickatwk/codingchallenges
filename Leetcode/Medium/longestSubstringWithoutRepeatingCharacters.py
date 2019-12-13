

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Time: O(N) | Space: (N) - the space is the size of the lastSeen dictionary
def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Represents the starting point of the substring
        idx = 0
        # Keeps track of the last seen character's position
        lastSeen = {}
        # Current maximum len of the substring
        max_substring_len = 0
        # The Secondary position where the substring will be build
        i = idx

        # Starting point of the new substring
        while (idx < len(s)):
            # Building the new substring
            while (i <= len(s)):
                # Terminate when you have reached the end of the string
                if i == len(s):
                    idx = len(s)
                    break
                # Check whether the current character is new or it was previously seen. Or if the current current's last seen is the same
                if s[i] not in lastSeen or lastSeen[s[i]] == i:
                    # Assign the last seen position to the character
                    lastSeen[s[i]] = i
                    # Check the len of the current substring
                    len_of_substring = (i+1) - idx
                    # Update the maximum len of the substring if the current substring is larger
                    if len_of_substring > max_substring_len:
                        max_substring_len = len_of_substring
                    # Increment the substring
                    i += 1
                else:
                    # Detect whether there is a change in the starting position of the substring
                    prev_idx = idx
                    # If the last seen positon of the character is larger than the current starting position, we need to begin from a new starting position - which is the last seen position of the character + 1
                    idx = max(idx, lastSeen[s[i]]+1)
                    # Update the new last seen position for the character
                    lastSeen[s[i]] = i
                    # If the starting position is unchanged, continue building the substring
                    if prev_idx == idx:
                        continue
                    # Otherwise, begin from the new starting position, and build the substring from there
                    break
    
        return max_substring_len