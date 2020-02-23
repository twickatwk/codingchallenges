
import math

# Time: O(N Log N) | Space: O(N)
def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        if len(deck) == 1 or len(deck) == 0:
            return False
        
        cards = {}
        
        for card in deck:
            if card in cards:
                cards[card] += 1
            else:
                cards[card] = 1
        
        a = None
        b = None
        greatestCommonFactor = None
        
        for card in cards:
            if a is None:
                a = cards[card]
                continue
            if b is None:
                b = cards[card]
                greatestCommonFactor = math.gcd(a, b)
                if greatestCommonFactor == 1:
                    return False
                continue
            
            # update the new card to compare
            b = cards[card]
            # so every single card needs to have a great common factor with the previous card, else
            # there will be no partition of cards
            greatestCommonFactor = math.gcd(greatestCommonFactor, b)
            if greatestCommonFactor == 1:
                return False
        
        return True
        