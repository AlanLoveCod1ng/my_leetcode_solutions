class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        matrix = [[0 for i in range(col)] for j in range(row)]
        matrix[0][0] = 1
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j]=0
                    continue
                if i>0:
                    matrix[i][j]+=matrix[i-1][j]
                if j>0:
                    matrix[i][j]+=matrix[i][j-1]
        return matrix[row-1][col-1]