class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        positions = [[startRow,startColumn]]
        mod = 10**9+7
        dp = [[0]*n for _ in range(m)]
        dp[startRow][startColumn] = 1
        result = 0
        for z in range(maxMove):
            tempdp = [[0]*n for _ in range(m)]
            for i in range(len(dp)):
                for j in range(len(dp[0])):
                    if i == 0:
                        result = (result+dp[i][j])%mod
                    if i == m-1:
                        result = (result+dp[i][j])%mod
                    if j == 0:
                        result = (result+dp[i][j])%mod
                    if j == n-1:
                        result = (result+dp[i][j])%mod
                    if i != 0:
                        tempdp[i][j] += dp[i-1][j]
                    if j != 0:
                        tempdp[i][j] += dp[i][j-1]
                    if i != m-1:
                        tempdp[i][j] += dp[i+1][j]
                    if j != n-1:
                        tempdp[i][j] += dp[i][j+1]
            dp = tempdp
        return result
        



    