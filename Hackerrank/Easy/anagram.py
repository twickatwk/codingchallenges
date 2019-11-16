# https://www.hackerrank.com/challenges/anagram/problem

# Time: O(N) | Space: O(N) | Dictionary
def anagram(s):
    if len(s) % 2 == 1:
        return -1
    s1 = s[0:len(s)//2]
    s2 = s[len(s)//2:len(s)]
    characters = {}
    additionalCharacters = 0
    for character in s2:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    
    for character in s1:
        if character in characters:
            characters[character] -= 1
            if characters[character] < 0:
                additionalCharacters += 1

        else:
            continue
    return sum(characters.values()) + additionalCharacters

def test_anagram():
    assert anagram("fdhlvosfpafhalll") == 5, "This should be 5"
    print("Everything is correct")

test_anagram()
