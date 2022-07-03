class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [[1,1] for _ in range(len(nums))]
        maxValue = 1
        for i in range(1,len(nums)):
            for j in range(i,-1, -1):
                if nums[j]>nums[i]:
                    dp[i][0] = max(dp[j][1]+1,dp[i][0])
                if nums[j]<nums[i]:
                    dp[i][1] = max(dp[j][0]+1,dp[i][1])
            maxValue = max(maxValue,dp[i][0],dp[i][1])
        return maxValue
                    
                    