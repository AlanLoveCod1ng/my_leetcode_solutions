class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_indices = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_indices.append(i)
        if len(zero_indices) <= k:
            return len(nums)
        #sliding window
        start = 0
        end = start+k-1
        max_len = 0
        res = 0
        while end < len(zero_indices):
            #index ahead of sliding
            start_1 = -1
            if start-1 >= 0:
                start_1 = zero_indices[start-1]
            end_1 = len(nums)
            if end + 1 < len(zero_indices):
                end_1 = zero_indices[end+1]
            length_1 = end_1 - start_1 - 1
            res = max(length_1,res)
            start+=1
            end +=1
        return res