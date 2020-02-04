
class SuffixTrieNode:
    def __init__(self):
        
        self.children = [None] * 26

    def insertSuffix(self, string):
        
        # if the string has more characters
        if (len(string) > 0):

            cIndex = ord(string[0]) - ord('a')

            if self.children[cIndex] == None:
                self.children[cIndex] = SuffixTrieNode()
            
            # Recur for the next suffix
            self.children[cIndex].insertSuffix(string[1:])

class SuffixTrie:

    def __init__(self, string):
        self.max_char = 26
        self.root = SuffixTrieNode()

        for i in range(len(string)):
            self.root.insertSuffix(string[i:])
        
    def countNodesInTrie(self, node):
        
        # if all nodes have been processed
        if node is None:
            return 0

        count = 0

        for i in range(26):
            if node.children[i] is not None:
                count += self.countNodesInTrie(node.children[i])

        return (1+count)
    
    def getNodesInTrie(self):
        return self.countNodesInTrie(self.root)
    

def countDistinctSubstring(string):

    sTrie = SuffixTrie(string)

    return sTrie.getNodesInTrie()

print(countDistinctSubstring('ababa'))

