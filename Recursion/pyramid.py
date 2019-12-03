
# Write a function that draws a side of a pyramid based on a given height using recursion
# Input: 4
# Output: 

#
##
###
####


def drawPyramid(height):
    
    if height == 0:
        return
    
    drawPyramid(height-1)
    for i in range(height):
        print("#", end="")
    print()
    return

drawPyramid(4)
        
