# Time: O(N) | Space O(N)
def checkMagazine(magazine, note):
    wordsInMag = {}
    for word in magazine:
        if word in wordsInMag:
            wordsInMag[word] += 1
        else:
            wordsInMag[word] = 1
    for word in note:
        if word in wordsInMag:
            wordsInMag[word] -= 1
            if wordsInMag[word] < 0:
                print("No")
                return
        else:
            print("No")
            return
    print("Yes")