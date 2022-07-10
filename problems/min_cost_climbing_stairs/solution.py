class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [math.inf]*(len(cost)+2)
        cost.append(0)
        dp[0] = 0
        for i in range(len(dp)-1):
            if i+1 < len(dp):
                dp[i+1] = min(dp[i+1],dp[i]+cost[i])
            if i+2 < len(dp):
                dp[i+2] = min(dp[i+2],dp[i]+cost[i+1])
        return dp[-1]