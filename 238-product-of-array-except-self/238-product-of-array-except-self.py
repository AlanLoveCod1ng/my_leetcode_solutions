class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        record = [1]*len(nums)
        result = [1]*len(nums)
        record[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            record[i] = record[i+1]*nums[i]
        for i in range(len(nums)):
            result[i] *= prefix
            if i != len(nums)-1:
                result[i] *= record[i+1]
            prefix *=nums[i]
        return result