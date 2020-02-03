
# Time: O(N) | Space: O(1)
def pokerHandCombination(arr):

    # write your codes here
    suits = {}
    ranks = {}
    isFlush = False
    isPairs = False
    isTwoPairs = False
    isThreeOfKind = False
    isFourOfKind = False
    isFullHouse = False
    isRoyal = True
    
    royal = {'1': True, '13': True, '12': True , '11': True, '10': True}
    
    for card in arr:
        rank = card[:-1]
        suit = card[-1]
        if rank == 'A':
            rank = '1'
        if rank == 'J':
            rank = '11'
        if rank == 'Q':
            rank = '12'
        if rank == 'K':
            rank = '13'
        
        # if any of the rank is not in royal, set it royal to false
        if rank not in royal:
            isRoyal = False
        
        # counting the suits
        if suit in suits:
            suits[suit] += 1
        else:
            suits[suit] = 1
        
        # counting the ranks
        if rank in ranks:
            ranks[rank] += 1
            if ranks[rank] == 3:
                isThreeOfKind = True
            if ranks[rank] == 4:
                isFourOfKind = True
        else:
            ranks[rank] = 1
        
    # if there is only one item in the suits dictionary, it means all of them are the same
    if len(suits) == 1:
        isFlush = True

    # 2 items - 4 of a kind
    # 3 items - Two Pairs/Three of a Kind
    # 4 items - 1 Pair

    if len(ranks) == 2:
        if not isFourOfKind:
            isFullHouse = True
    if len(ranks) == 3:
        if not isThreeOfKind:
            isTwoPairs = True
    if len(ranks) == 4:
        isPairs = True
    
    
        
    order = list(ranks)
    order_int = [int(i) for i in order] 
    order_int.sort()
    # check whether a straight
    prev = order_int[0]
    isStraight = True
    
    for i in range(1, len(order_int)):
        if (prev+1) != order_int[i]:
            isStraight = False
            break
        prev = order_int[i]
    
    if isRoyal and isFlush:
        print("Royal Flush")
        
    elif isFlush and isStraight:
        print("Straight Flush")
        
    elif isFourOfKind:
        print("Four of a Kind")
        
    elif isFullHouse:
        print("Full House")
    
    elif isFlush:
        print("Flush")
        
    elif isRoyal:
        print("Straight")
        
    elif isStraight:
        print("Straight")
        
    
    elif isThreeOfKind:
        print("Three of a Kind")
        
    
    elif isTwoPairs:
        print("Two Pair")
        
    elif isPairs:
        print("Pair")
        
    else:
        print("High Card")


