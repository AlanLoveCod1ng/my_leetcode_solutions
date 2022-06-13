class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        matrix = [[0 for i in range(col)] for j in range(row)]
        matrix[0][0] = grid[0][0]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    matrix[i][j] = matrix[i][j]
                elif i == 0 and j != 0:
                    matrix[i][j] = matrix[i][j-1]+grid[i][j]
                elif j == 0 and i != 0:
                    matrix[i][j] = matrix[i-1][j]+grid[i][j]
                else:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1])+grid[i][j]
        return matrix[row-1][col-1]