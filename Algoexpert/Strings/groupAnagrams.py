# https://www.algoexpert.io/questions/Group%20Anagrams

# Write a function that takes in an array of strings and returns a list of groups of anagrams.
# Anagrams are strings made up of exactly the same letters, where osrder doesn't matter.

# Time: O(w*n log n) | Space: O(wn)
def groupAnagrams(words):
    # Write your code here.
	
	dict_words = {}
	for word in words:
		sorted_word = ''.join(sorted(word))
		if sorted_word in dict_words:
			dict_words[sorted_word].append(word)
		else:
			dict_words[sorted_word] = [word]
	result = []
	for value in dict_words.values():
		result.append(value)
		
	return result

print(groupAnagrams(["yo", "act", "flop", "tac", "cat", "oy", "olfp"]))
