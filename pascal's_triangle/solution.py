class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            result.append([])
            for j in range(i+1):
                if i == 0:
                    result[i].append(1)
                    continue
                result[i].append(0)
                if j != 0:
                    result[i][j]+=result[i-1][j-1]
                if j != i:
                    result[i][j]+=result[i-1][j]
        return result