class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevMin = nums[0]
        prevMax = nums[0]
        maxValue = nums[0]
        for i in range(1,len(nums)):
            currentMin = min(nums[i],prevMin*nums[i],prevMax*nums[i])
            currentMax = max(nums[i],prevMin*nums[i],prevMax*nums[i])
            prevMin = currentMin
            prevMax = currentMax
            maxValue = max(currentMax,maxValue)
        return maxValue