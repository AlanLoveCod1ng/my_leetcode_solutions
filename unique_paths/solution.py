class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for i in range(n)] for j in range(m)]
        matrix[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    matrix[i][j]+=matrix[i-1][j]
                if j > 0:
                    matrix[i][j]+=matrix[i][j-1]
        return matrix[m-1][n-1]