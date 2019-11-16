# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

# Time: O(N) | Space: O(N) | Dictionary
def sherlockAndAnagrams(s):
    size = 0
    countOfanagram = 0
    while size < len(s)-1:
        for i in range(len(s)-1):
            characters = {}
            if i+size+1 <= len(s)-1:
                word = s[i:i+size+1]
                
                for c in word:
                    if c in characters:
                        characters[c] += 1
                    else:
                        characters[c] = 1
            else:
                break
            for j in range(i+1, len(s)):
                characters2 = characters.copy()
                if j+size+1 <= len(s):
                    word2 = s[j:j+size+1]
                    for c in word2:
                        if c in characters2:
                            if characters2[c] == 0:
                                break
                            characters2[c] -= 1
                        else:
                            continue
                    if sum(characters2.values()) == 0:
                        countOfanagram += 1 
        size += 1
    return countOfanagram

def test_sherlockAndAnagrams():
    s = "ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel"
    assert sherlockAndAnagrams(s) == 399, "Expected: 399 | Output: " + str(sherlockAndAnagrams(s))
    print("Output is correct! Expected: 399 | Output: 399")

test_sherlockAndAnagrams()