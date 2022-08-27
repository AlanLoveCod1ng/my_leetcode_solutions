class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        len_pos = [0]*len(nums)
        len_neg = [0]*len(nums)
        if nums[0] > 0:
            len_pos[0] = 1
        if nums[0] < 0:
            len_neg[0] = 1
        res = len_pos[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                len_pos[i] = len_pos[i-1] + 1
                len_neg[i] = len_neg[i-1] + 1 if len_neg[i-1] != 0 else 0
                res = max(res,len_pos[i])
            elif nums[i] < 0:
                len_pos[i] = len_neg[i-1] + 1 if len_neg[i-1] != 0 else 0
                len_neg[i] = len_pos[i-1] + 1
                res = max(res,len_pos[i])
            else:
                len_neg[i] = 0
                len_pos[i] = 0
        return res