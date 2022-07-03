class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        indices = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashtable:
                indices = [hashtable[complement],i]
                return indices
            hashtable[nums[i]] = i
        return indices