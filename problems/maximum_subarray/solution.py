class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for x in range(len(nums))]
        dp[0] = nums[0]
        result = dp[0]
        for i in range(len(nums)):
            if i == 0:
                continue
            dp[i] = max(nums[i],nums[i]+dp[i-1])
            result = max(dp[i],result)
        return result