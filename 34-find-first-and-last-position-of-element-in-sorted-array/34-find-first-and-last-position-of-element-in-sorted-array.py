class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.first = -1
        self.last = -1
        if len(nums) == 0:
            return [-1,-1]
        self.binarySearch(nums,0,len(nums)-1,target,0)
        return [self.first,self.last]
        
    def binarySearch(self, nums, start, end, target, state):
        if start > end:
            return
        if start == end and nums[start] != target:
            return
        mid = int((start+end)/2)
        if nums[mid] < target:
            self.binarySearch(nums,mid+1,end,target,0)
        elif nums[mid]> target:
            self.binarySearch(nums,start,mid-1,target,0)
        else:
            if state != 2:
                if mid == 0:
                    self.first = mid
                elif nums[mid-1] == target:
                    self.binarySearch(nums,start,mid-1,target,1)
                else:
                    self.first = mid
            if state != 1:
                if mid == len(nums)-1:
                    self.last = mid
                elif nums[mid+1] == target:
                    self.binarySearch(nums,mid+1,end,target,2)
                else:
                    self.last = mid
        
        