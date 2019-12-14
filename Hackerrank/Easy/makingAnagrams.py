
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Time: O(N) | Space: O(N)
def makeAnagram(a, b):
    
    dict_words = {}
    count = 0
    for char in a:
        if char in dict_words:
            dict_words[char] += 1
        else:
            dict_words[char] = 1
    
    for char in b:
        if char in dict_words:
            if dict_words[char] == 0:
                count += 1
            else:
                dict_words[char] -= 1
        else:
            count += 1
    
    for value in dict_words.values():
        count += value
    
    return count