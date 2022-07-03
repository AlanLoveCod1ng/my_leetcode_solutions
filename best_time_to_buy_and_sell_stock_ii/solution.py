class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                continue
            profit+=max(0,prices[i]-prices[i-1])
        return profit