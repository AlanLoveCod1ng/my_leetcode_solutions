class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        maxArea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    continue
                if j == 0:
                    dp[i][j] = 1 if matrix[i][j] == "1" else 0
                else:
                    dp[i][j] = dp[i][j-1]+1
                
                maxWidth = dp[i][j]
                height = 1
                for z in range(i, -1, -1):
                    if dp[z][j] == 0:
                        break
                    maxWidth = min(maxWidth, dp[z][j])
                    height = i-z+1
                    maxArea = max(maxWidth*height, maxArea)
        return maxArea