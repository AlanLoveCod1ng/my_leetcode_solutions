class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        prev_arr = nums
        next_arr = [0]*(len(prev_arr)-1)
        while len(next_arr) > 0:
            for i in range(len(next_arr)):
                next_arr[i] = (prev_arr[i]+prev_arr[i+1])%10
            prev_arr = next_arr
            next_arr = [0]*(len(prev_arr)-1)
        return prev_arr[0]