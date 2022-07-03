class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k==0:
            return 0

        if 2*k > len(prices):
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
            return res

        dp = [[[-math.inf]*2 for _ in range(k+1)] for _ in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]
        for i in range(1,len(prices)):
            for j in range(k+1):
                dp[i][j][1] = dp[i-1][j][1]
                #buy
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j-1][0] - prices[i], dp[i-1][j][1])
                #sell
                dp[i][j][0] = max(dp[i-1][j][1]+prices[i], dp[i-1][j][0])
        res = max(dp[len(prices)-1][j][0] for j in range(k+1))
        return res