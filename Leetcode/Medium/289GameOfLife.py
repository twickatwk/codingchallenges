
from copy import copy, deepcopy
class Solution(object):

    # Time: O(MN) | Space: O(MN)
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        
        aux = deepcopy(board)
        
        for i in range(len(aux)):
            for j in range(len(aux[i])):
                valueOfCell = aux[i][j]
                noOfLiveNeighbours = self.getLiveNeighbours(aux, i, j)
                
                if valueOfCell == 0 and noOfLiveNeighbours == 3:
                    board[i][j] = 1
                elif valueOfCell == 1 and (noOfLiveNeighbours < 2 or noOfLiveNeighbours > 3):
                    board[i][j] = 0
                elif valueOfCell == 1 and (noOfLiveNeighbours == 2 or noOfLiveNeighbours == 3):
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        
        return board
    
    def getLiveNeighbours(self, board, i, j):
        
        row = i
        col = j
        
        count = 0
        
        # verticals and horizontals
        if row - 1 >= 0 and board[row-1][col] == 1:
            count += 1
        if row + 1 < len(board) and board[row+1][col] == 1:
            count += 1
        if col - 1 >= 0 and board[row][col-1] == 1:
            count += 1
        if col + 1 < len(board[row]) and board[row][col+1] == 1:
            count += 1
        
        # diagionals
        if row - 1 >= 0 and col - 1 >= 0 and board[row-1][col-1] == 1:
            count += 1
        if row - 1 >= 0 and col + 1 < len(board[row]) and board[row-1][col+1] == 1:
            count += 1
        if row + 1 < len(board) and col-1 >= 0 and board[row+1][col-1] == 1:
            count += 1
        if row + 1 < len(board) and col + 1 < len(board[row]) and board[row+1][col+1]:
            count += 1
        
        return count