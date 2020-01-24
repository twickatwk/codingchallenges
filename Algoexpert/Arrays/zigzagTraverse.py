
# Time: O(MN) | Space: O(M+N)
def zigzagTraverse(A):
    # Write your code here.

    row = 0
    col = 0
    toggle = True
    result = [A[row][col]]
    start = True

    while (start):
        if toggle:
            if row + 1 < len(A):
                row, col = traverseDiaUp(A, row+1, col, result)
                toggle = not toggle
            elif col + 1 < len(A[row]):
                row, col = traverseDiaUp(A, row, col+1, result)
                toggle = not toggle
            else:
                return result
        else:
            if col + 1 < len(A[row]):
                row, col = traverseDiaDown(A, row, col+1, result)
                toggle = not toggle
            elif row + 1 < len(A):
                row, col = traverseDiaDown(A, row+1, col, result)
                toggle = not toggle
            else:
                return result
            
    return result

def traverseDiaDown(A, row, col, result):
    result.append(A[row][col])

    while row+1 < len(A) and col-1 >= 0:
        row += 1
        col -= 1
        print("Traversing Down: " + str(row) + " " + str(col))
        result.append(A[row][col])

    print("Ending Diagional Down Position: " + str(row) + " " + str(col))

    return row, col

def traverseDiaUp(A, row, col, result):
    result.append(A[row][col])

    while row - 1 >= 0 and col + 1 < len(A[row]):
        row -= 1
        col += 1
        print("Traversing Up: " + str(row) + " " + str(col))
        result.append(A[row][col])
    
    print("Ending Diagional Up Position: " + str(row) + " " + str(col))
    return row, col

A = [[1],[2],[3]]
print(zigzagTraverse(A))