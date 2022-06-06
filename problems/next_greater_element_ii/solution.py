class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        unassigned = []
        result = []
        record = [0]*len(nums)
        for i in range(len(nums)):
            while len(unassigned) != 0:
                prev = unassigned[-1]
                if nums[i] > nums[prev]:
                    record[prev] = nums[i]
                    unassigned.pop()
                else:
                    break
            unassigned.append(i)
        for i in range(len(nums)):
            while len(unassigned) != 0:
                prev = unassigned[-1]
                if nums[i] > nums[prev]:
                    record[prev] = nums[i]
                    unassigned.pop()
                else:
                    break
        for i in unassigned:
            record[i] = -1
        return record