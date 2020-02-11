
# Time: O(MN) | Space: O(MN)
def maxAreaOfIsland(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
        
    maxIslandSize = 0
    # this keeps tracks of the nodes that have been visited
    aux = [[False for value in row] for row in grid]
    # check through every node in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # for nodes that are land, simply toggle them as visited and pass them
            if grid[i][j] == 0:
                aux[i][j] == True
                continue
            # skip nodes that have been visted
            if aux[i][j] == True:
                continue
            # for nodes that are 1, start the BFS search, initialing the current node as visited, and size of river to be 0
            stack = [[i,j]]
            aux[i][j] = True
            size = 0
            # print("Start of DFS")
            while len(stack):
                node = stack.pop()
                # get all the nodes that are connected to the current node that are 1 in value
                neighbours = self.getNeighbours(node[0],node[1],aux, grid)
                # add those neighbours into the stack, which will be visited later on
                for neighbour in neighbours:
                    
                    stack.append(neighbour)
                
                # print(node)
                
                # increment the size of the connected river for each of the node that you pop out of the stack
                size += 1
            # after each BFS search, update the maximum size of the river
            if size > maxIslandSize:
                maxIslandSize = size
            
            
    return maxIslandSize

def getNeighbours(self, row, col, aux, grid):
    
    result = []
    
    # up
    if row-1 >= 0 and grid[row-1][col] == 1 and aux[row-1][col] == False:
        result.append([row-1, col])
        aux[row-1][col] = True
    # down
    if row+1 < len(grid) and grid[row+1][col] == 1 and aux[row+1][col] == False:
        result.append([row+1, col])
        aux[row+1][col] = True
    # left
    if col-1 >= 0 and int(grid[row][col-1]) == 1 and aux[row][col-1] == False:
        result.append([row, col-1])
        aux[row][col-1] = True
    # right
    if col+1 < len(grid[row]) and int(grid[row][col+1]) == 1 and aux[row][col+1] == False:
        result.append([row, col+1])
        aux[row][col+1] = True 
    
    return result

