class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        self.backtrace([],0,nums)
        return self.res
    def backtrace(self, current, index, nums):
        for i in range(index,len(nums)):
            next_ = current+[nums[i]]
            self.res.append(next_)
            self.backtrace(next_,i+1,nums)
            