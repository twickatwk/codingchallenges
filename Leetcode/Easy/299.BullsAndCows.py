
# Time O(N) | Space: O(N)
def getHint(secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        secretDict = {}
        guessDict = {}
        bulls = 0
        cows = 0
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                continue
            
            if secret[i] in guessDict:
                if guessDict[secret[i]] > 0:
                    guessDict[secret[i]] -= 1
                    cows += 1
                else:
                    if secret[i] in secretDict:
                        secretDict[secret[i]] += 1
                    else:
                        secretDict[secret[i]] = 1
            else:
                if secret[i] in secretDict:
                        secretDict[secret[i]] += 1
                else:
                    secretDict[secret[i]] = 1
                        
            if guess[i] in secretDict:
                if secretDict[guess[i]] > 0:
                    secretDict[guess[i]] -= 1
                    cows += 1
                else:
                    if guess[i] in guessDict:
                        guessDict[guess[i]] += 1
                    else:
                        guessDict[guess[i]] = 1
            else:
                if guess[i] in guessDict:
                        guessDict[guess[i]] += 1
                else:
                    guessDict[guess[i]] = 1
                    
        
        return str(bulls) + 'A' + str(cows) + "B"