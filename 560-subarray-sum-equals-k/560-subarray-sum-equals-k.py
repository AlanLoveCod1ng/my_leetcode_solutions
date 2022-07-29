class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = [0]*len(nums)
        hashtable = {0:1}
        result = 0
        for i in range(len(nums)):
            if i != 0:
                sums[i] = sums[i-1] + nums[i]
            else:
                sums[i] = nums[i]
            complement = sums[i] - k
            result += hashtable.get(complement,0)
            hashtable[sums[i]] = hashtable.get(sums[i],0)+1

        return result