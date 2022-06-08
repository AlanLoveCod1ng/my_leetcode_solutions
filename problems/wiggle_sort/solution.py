class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sortedNums = sorted(nums)
        temp = []
        start = 0
        end = len(sortedNums)-1
        while start<=end:
            if start == end:
                temp.append(sortedNums[start])
                break
            else:
                temp.append(sortedNums[start])
                temp.append(sortedNums[end])
                start+=1
                end-=1
        for i in range(len(temp)):
            nums[i] = temp[i]