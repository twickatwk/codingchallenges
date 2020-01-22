import collections
import copy

# Time: O(MN) | Space: O(MN)
def orangesRotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    
    # this stores the after version of the grid after all rotting has taken effect
    after = copy.deepcopy(grid)
    # this stores the time it takes for the rot to reach that cell
    time = [[None for value in row] for row in grid]

    # this stores the minimum time it will take for the rot to reach every single cell
    maxTimeElapsed = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            currentNode = [i, j]
            # if the current cell is an empty or fresh apple, skip it
            if grid[i][j] == 0 or grid[i][j] == 1:
                continue
            # otherwise, generate a queue to start the rotting effect
            nodesToVisit = collections.deque([[i, j]])
            # from this current position, the elapsed time starts from 0
            currentElapsedTime = 0
            # this helps to identify whether a particular cell has already been visited, preventing infinite loop
            aux = [[False for value in row] for row in grid]
            # the first rotten apple has 0 elapsed time
            time[i][j] = currentElapsedTime

            aux[i][j] = True
            
            # keep visiting every single neighbour with fresh apples
            while len(nodesToVisit) > 0:
                
                currentNode = nodesToVisit.popleft()
                
                neighbours = getAllNeighbours(currentNode, grid, aux, after)
                
                for neighbour in neighbours:
                    # if there is no current speed of rot for the neighbour, set the neighbour's rotten time to +1 of the current node
                    if time[neighbour[0]][neighbour[1]] is None:
                        time[neighbour[0]][neighbour[1]] = time[currentNode[0]][currentNode[1]]+1
                    # otherwise, you will have to compare whether there is a faster way for the rot to reach its neighbour
                    else:
                        if time[neighbour[0]][neighbour[1]] > time[currentNode[0]][currentNode[1]]+1:
                            time[neighbour[0]][neighbour[1]] = time[currentNode[0]][currentNode[1]]+1
                    # add that neighbour to the queue
                    nodesToVisit.append(neighbour) 
    
    # checks whether is there any apples that will never be rotten, using the "after" matrix
    for i in range(len(after)):
        for j in range(len(after[i])):
            if after[i][j] == 1:
                return -1
    
    # checks the minimum time for the rot to cover the entire grid of apples, which is the maximum time it takes for the last apple to be rotten
    for i in range(len(time)):
        for j in range(len(time[i])):
            if time[i][j] != None and time[i][j] > maxTimeElapsed:
                maxTimeElapsed = time[i][j]
    
    return maxTimeElapsed

def getAllNeighbours(currentNode, grid, aux, after):
    row = currentNode[0]
    col = currentNode[1]
    neighbours = []
    
    if col-1 >= 0 and grid[row][col-1] == 1 and aux[row][col-1] == False:
        aux[row][col-1] = True
        after[row][col-1] = 2
        neighbours.append([row,col-1])
        
    if col+1 < len(grid[row]) and grid[row][col+1] == 1 and aux[row][col+1] == False:
        aux[row][col+1] = True
        after[row][col+1] = 2
        neighbours.append([row,col+1])
    
    if row-1 >= 0 and grid[row-1][col] == 1 and aux[row-1][col] == False:
        aux[row-1][col] == False
        after[row-1][col] = 2
        neighbours.append([row-1,col])
    
    if row+1 < len(grid) and grid[row+1][col] == 1 and aux[row+1][col] == False:
        aux[row+1][col] = True
        after[row+1][col] = 2
        neighbours.append([row+1,col])
    
    return neighbours

print(orangesRotting([[2,1,1], [1,1,0], [0,1,1]]))