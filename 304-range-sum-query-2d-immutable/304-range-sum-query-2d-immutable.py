class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        sums = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(1,len(sums)):
            for j in range(1,len(sums[0])):
                sums[i][j] = sums[i-1][j]+sums[i][j-1] + matrix[i-1][j-1] - sums[i-1][j-1]
        self.sums = sums
        self.matrix= matrix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sums = self.sums
        a = sums[row2+1][col2+1]
        b = sums[row1][col2+1]
        c = sums[row2+1][col1]
        d = sums[row1][col1]
        return a - b - c + d


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)