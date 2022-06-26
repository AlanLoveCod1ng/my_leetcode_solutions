class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount+1)
        for i in range(1,len(dp)):
            if i in coins:
                dp[i] = 1
                continue
            minNum = -1
            if i == 249:
                a = 0
            for coinValue in coins:
                if coinValue > i:
                    continue
                if dp[i-coinValue] != -1:
                    if minNum == -1:
                        minNum = dp[i-coinValue]+1
                    minNum = min(minNum,dp[i-coinValue]+1)
            dp[i] = minNum
        return dp[-1]