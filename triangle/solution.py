class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        result = None
        for i in range(row):
            if i == 0:
                continue
            for j in range(len(triangle[i])):
                if j != 0 and j < len(triangle[i])-1:
                    triangle[i][j]+=min(triangle[i-1][j-1], triangle[i-1][j])
                elif j == 0:
                    triangle[i][j]+=triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j]+=triangle[i-1][j-1]
        for i in range(len(triangle[row-1])):
            if result == None:
                result = triangle[row-1][i]
            result = min(result, triangle[row-1][i])
        return result
                