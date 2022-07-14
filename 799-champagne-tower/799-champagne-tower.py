class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured]
        if query_row == 0:
            return 1 if poured >=1 else poured
        for i in range(1,query_row+1):
            temp = [0]*(len(dp)+1)
            for j in range(len(temp)):
                if j != 0:
                    if dp[j-1] > 1:
                        temp[j] += (dp[j-1]-1)/2
                if j < len(dp):
                    if dp[j] > 1:
                        temp[j] += (dp[j]-1)/2
            dp = temp
        return min(dp[query_glass], 1)