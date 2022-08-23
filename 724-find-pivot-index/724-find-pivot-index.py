class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # [1,8,3,4,5]
        # [1,9,12,16,21]
        # let assuming i = 1 
        # sum of left = prefix_sum[i-1] = prefix_sum[0] = 1
        # sum of right = prefix_sum[-1] - prefix_sum[i] = 12
        # let assuming i = 2 
        # sum of left = prefix_sum[i-1] = prefix_sum[1] = 9
        # sum of right = prefix_sum[-1] - prefix_sum[i] = 21 - 12 = 9
        # prefix_sum[i] = sum(arr[:i+1])
        # time: O(N) space: O(N)
        if len(nums) == 1:
            return 0
        sums = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                sums[0] = nums[0]
                continue
            sums[i] = sums[i-1] + nums[i]
        for i in range(len(nums)):
            sum_left = 0
            sum_right = sums[-1] - sums[i]
            if i != 0:
                sum_left = sums[i-1]
            if sum_left == sum_right:
                return i
        return -1