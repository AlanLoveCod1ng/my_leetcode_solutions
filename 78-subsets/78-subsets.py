class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        self.backtrace([],0,nums)
        return self.res
    def backtrace(self, current, index, nums):
        
        for i in range(index,len(nums)):
            current.append(nums[i])
            self.res.append(current[:])
            self.backtrace(current,i+1,nums)
            current.pop()
            