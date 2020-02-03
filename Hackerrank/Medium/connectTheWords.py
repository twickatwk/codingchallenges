
# Time: O(NL) | Space: O(N)
def connectWords(lst):
    # Write your code here. Remember to print out the output
    
    prevWord = lst[0]
    result = prevWord
    minOverlap = float('inf')
    if len(lst) == 1:
        print("['" + str(lst[0]) + "', 0]")
    else:
        for i in range(1, len(lst)):
            indexa = 0
            indexb = 0
            currentWord = lst[i]
            overlap = 0
            print(prevWord)
            print(currentWord)
            for j in range(len(prevWord)):
                if prevWord[j:] == currentWord[0:len(prevWord)-j]:
                    overlap = len(prevWord)-j
                    print(overlap)
                    break
            
            result += currentWord[overlap:]
            
            if overlap < minOverlap:
                minOverlap = overlap
            
            prevWord = currentWord
    
    print("['" + result + "', " + str(minOverlap) + "]")

connectWords(["syllable", "ble", "e", "ebe"])