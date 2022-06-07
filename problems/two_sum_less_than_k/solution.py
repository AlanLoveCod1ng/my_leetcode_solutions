class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        start = 0
        end = len(nums)-1
        maxValue = -1
        while start<end:
            temp = nums[start]+nums[end]
            if temp>=k:
                end-=1
            else:
                start+=1
                if temp>maxValue:
                    maxValue = temp
        return maxValue