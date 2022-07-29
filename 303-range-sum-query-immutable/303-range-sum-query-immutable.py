class NumArray:
    
    def __init__(self, nums: List[int]):
        sums = [0]*len(nums)
        sums[0] = nums[0]
        for i in range(1,len(sums)):
            sums[i] = nums[i] + sums[i-1]
        self.sums = sums
        self.nums = nums
    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right]-self.sums[left]+self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)