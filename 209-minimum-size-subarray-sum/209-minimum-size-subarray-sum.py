class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        result = math.inf
        sum_sofar = 0
        for i in range(len(nums)):
            sum_sofar += nums[i]
            while sum_sofar >= target:
                result = min(result,i-start+1)
                sum_sofar -= nums[start]
                start+=1
        return 0 if result == math.inf else result