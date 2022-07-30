class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero_sum = [0]*len(nums)
        one_sum = [0]*len(nums)
        result = 0
        zero_sum[0] = 1 if nums[0] == 0 else 0
        one_sum[0] = 1 if nums[0] == 1 else 0
        hashtable = {zero_sum[0]-one_sum[0]:0,0:-1}
        for i in range(1,len(nums)):
            zero_sum[i] = zero_sum[i-1]
            one_sum[i] = one_sum[i-1]
            if nums[i] == 1:
                one_sum[i]+=1
            else:
                zero_sum[i]+=1
            current_difference = zero_sum[i] - one_sum[i]
            result = max(result, i-hashtable.get(current_difference, i))
            if not current_difference in hashtable:
                hashtable[current_difference] = i
        return result
            