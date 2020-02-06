
# Time: O(N) | Space: O(N)
def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dictWords = {}
        
        for word in strs:
            new = list(word)
            new.sort()
            newWord = "".join(new)
            if newWord in dictWords:
                #print(word)
                dictWords[newWord].append(word)
                #print(dictWords)
            else:
                dictWords[newWord] = [word]
        
        result = []
        for value in dictWords.values():
            result.append(value)
        
        return result