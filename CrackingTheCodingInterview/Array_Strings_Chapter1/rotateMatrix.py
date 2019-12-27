
# 1.7 

# Time: O(N^2) | Space: O(1) - Swaps the individual cells
def rotateMatrix(matrix):
    # If the length of the matrx or its the NxN matrix, return false
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False

    N = len(matrix)

    for layer in range(N//2):
        first = layer
        last = N - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i] # Saves the top layer

            # Left to top
            matrix[first][i] = matrix[last-offset][first]

            # Right to left
            matrix[last-offset][first] = matrix[last][last-offset]

            # Right to bottom
            matrix[last][last-offset] = matrix[i][last]

            # Top to right
            matrix[i][last] = top

    print(matrix)

rotateMatrix([['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']])