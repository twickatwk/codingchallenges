
# Time: O(MN) | Space: O(MN)
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    
    aux = [[False for value in row] for row in grid]
    
    
    totalIslands = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if aux[i][j] == True:
                continue
            aux[i][j] = True
            if grid[i][j] == "0":
                continue
            
            stack = [[i, j]]
            totalIslands += 1
            
            while(len(stack) > 0):
                currentNode = stack.pop()
                
                neighbours = getNeighbours(currentNode, grid, aux)
                
                for neighbour in neighbours:
                    stack.append(neighbour)
    
    return totalIslands
    
def getNeighbours(currentNode, grid, aux):
    row = currentNode[0]
    col = currentNode[1]
    neighbours = []
    
    # verticals and horizontals
    if row - 1 >= 0 and aux[row-1][col] != True and grid[row-1][col] == "1":
        aux[row-1][col] = True
        neighbours.append([row-1, col])
    if row + 1 < len(grid) and grid[row+1][col] != True and grid[row+1][col] == "1":
        aux[row+1][col] = True
        
        neighbours.append([row+1, col])
    if col - 1 >= 0 and aux[row][col-1] != True and grid[row][col-1] == "1":
        aux[row][col-1] = True
        neighbours.append([row, col-1])
    if col + 1 < len(grid[row]) and aux[row][col+1] != True and grid[row][col+1] == "1":
        aux[row][col+1] = True
        neighbours.append([row, col+1])
        
    # diagonals
    
    if row - 1 >= 0 and col - 1 >= 0 and aux[row-1][col-1] != True and grid[row-1][col-1] == 1:
        aux[row-1][col-1] = True
        neighbours.append([row-1, col-1])
    if row - 1 >= 0 and col + 1 < len(grid[row]) and aux[row-1][col+1] != True and  grid[row-1][col+1] == 1:
        aux[row-1][col+1] = True
        neighbours.append([row-1, col+1])
    if row + 1 < len(grid) and col - 1 >= 0 and aux[row+1][col-1] != True and grid[row+1][col-1] == 1:
        aux[row+1][col-1] = True
        neighbours.append([row+1, col-1])
    if row + 1 < len(grid) and col + 1 < len(grid[row]) and aux[row+1][col+1] != True and grid[row+1][col+1] == 1:
        aux[row+1][col+1] = True
        neighbours.append([row+1, col+1])
    
    return neighbours


print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))