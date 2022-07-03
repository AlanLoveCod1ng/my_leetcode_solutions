class Solution:
    def trap(self, height: List[int]) -> int:
        dp = [0 for x in range(len(height))]
        prevHeight = 0
        result = 0
        for i in range(len(height)):
            prevHeight = max(prevHeight, height[i])
            dp[i] = prevHeight - height[i]
        prevHeight = 0
        for i in range(len(height)-1, -1, -1):
            prevHeight = max(prevHeight, height[i])
            dp[i] = min(prevHeight - height[i], dp[i])
            result += dp[i]
        return result
            
                