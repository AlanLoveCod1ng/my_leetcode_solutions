class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex+1):
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
        return result[-1]