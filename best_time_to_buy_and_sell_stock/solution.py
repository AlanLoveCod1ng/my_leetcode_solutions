class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        dp = [0]*len(prices)
        for i in range(len(prices)):
            if i == 0:
                dp[i] = 0
                continue
            dp[i] = max(0,prices[i]-prices[i-1]+dp[i-1])
            if dp[i] > maximum:
                maximum = dp[i]
        return maximum