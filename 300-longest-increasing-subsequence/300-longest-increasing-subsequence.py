class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        res = 0
        for i in range(len(nums)):
            maxi = 0
            for j in range(0,i):
                if nums[j] < nums[i]:
                    maxi = max(maxi,dp[j])
            dp[i] += maxi
            res = max(res,dp[i])
        return res
        