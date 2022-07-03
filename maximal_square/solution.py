class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                maxArea = max(maxArea,matrix[i][j])
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if not matrix[i][j]:
                    continue
                matrix[i][j]+=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
                maxArea = max(maxArea, matrix[i][j]**2)
        return maxArea