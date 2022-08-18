class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp_matrix = [[0]*(len(grid[0])+1) for _ in range(len(grid)+1)]
        for i in range(len(dp_matrix)):
            dp_matrix[i][0]=math.inf
        for i in range(len(dp_matrix[0])):
            dp_matrix[0][i] = math.inf
        for i in range(1,len(dp_matrix)):
            for j in range(1,len(dp_matrix[0])):
                dp_matrix[i][j] = grid[i-1][j-1]
                if i ==1 and j == 1:
                    continue
                dp_matrix[i][j] += min(dp_matrix[i][j-1],dp_matrix[i-1][j])
        return dp_matrix[-1][-1]
                