import heapq
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dpLeft = [0]*len(prices)
        dpRight = [0]*len(prices)
        maxValue = 0
        minPrice = prices[0]
        for i in range(1,len(prices)):
            dpLeft[i] = max(maxValue, prices[i]-minPrice)
            maxValue = max(maxValue,dpLeft[i])
            minPrice = min(prices[i],minPrice)
        maxValue = 0
        maxPrice = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            dpRight[i] = max(maxValue, maxPrice-prices[i])
            maxValue = max(maxValue,dpRight[i])
            maxPrice = max(prices[i],maxPrice)
        result = 0
        for i in range(len(prices)-1):
            result = max(dpLeft[i]+dpRight[i+1],result)
        result = max(result, dpLeft[-1],dpRight[0])
        return result