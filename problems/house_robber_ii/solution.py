class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums1 = nums[0:len(nums)-1]
        dp = [[0,0]for _ in range(len(nums1))]
        dp[0] = [nums1[0],0]
        for i in range(1,len(nums1)):
            dp[i][0] = dp[i-1][1]+nums1[i]
            dp[i][1] = max(dp[i-1][0],dp[i-1][1])
        result1 = max(dp[-1][0],dp[-1][1])
        nums2 = nums[1:len(nums)+1]
        dp = [[0,0]for _ in range(len(nums2))]
        dp[0] = [nums2[0],0]
        for i in range(1,len(nums2)):
            dp[i][0] = dp[i-1][1]+nums2[i]
            dp[i][1] = max(dp[i-1][0],dp[i-1][1])
        result2 = max(dp[-1][0],dp[-1][1])
        return max(result1,result2)