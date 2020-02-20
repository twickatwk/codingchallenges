
# This solution can still be improved
# Time:O (N*K) | Space: O(N)

import collections
def licenseKeyFormatting(S, K):
        
        count = 0
        result = []
        de = collections.deque([])
        
        for i in range(len(S)-1, -1, -1):
            
            if S[i] == '-':
                continue
            
            count += 1
            de.appendleft(S[i].upper())
            
            if count == K:
                result.append("".join(list(de)))
                de = collections.deque([])
                count = 0
        
        if len(list(de)):
            result.append("".join(list(de)))
        
        result = list(reversed(result))
        
        return "-".join(result)