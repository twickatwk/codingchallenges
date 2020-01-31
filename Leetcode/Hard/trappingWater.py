

# Time: O(N) | Space: O(N)
def trappingWater(h):
    
    # you need a minimum of len 3 to at least trap water
    if len(h) < 3:
        return 0
    
    leftBoundary = [None] * len(h)
    rightBoundary = [None] * len(h)
    capacity = []
    maxHeight = 0
    
    # find the maximum left boundary's height at the current position
    for i in range(len(h)):
        if h[i] > maxHeight:
            maxHeight = h[i]
            leftBoundary[i] = maxHeight
        else:
            leftBoundary[i] = maxHeight


    maxHeight = 0
    
    # find the maximum right boundary's height at the current position
    for i in range(len(h)-1, -1, -1):
        if h[i] > maxHeight:
            maxHeight = h[i]
            rightBoundary[i] = maxHeight
        else:
            rightBoundary[i] = maxHeight

    # based on the current position's left and right boundary, determine the minimum boundary height, the difference between min boundary height and the height of the current building is the capacity of water trapped
    for i in range(1, len(h)-1):
        capacity.append(min(leftBoundary[i], rightBoundary[i]) - h[i])


    return sum(capacity)

print(trappingWater([0,1,0,2,1,0,1,3,2,1,2,1]))
