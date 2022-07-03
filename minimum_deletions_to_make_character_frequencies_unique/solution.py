class Solution:
    def minDeletions(self, s: str) -> int:
        hashtable = {}
        for i in range(len(s)):
            hashtable[s[i]] = hashtable.get(s[i],0)+1
        nums = []
        for i in hashtable:
            nums.append(hashtable[i])
        nums = sorted(nums)
        deleted = 0
        for i in range(len(nums)-2,-1,-1):
            origin = nums[i]
            if nums[i]>=nums[i+1]:
                nums[i] = nums[i+1]-1
                deleted+=origin-nums[i]
                if nums[i] == 0:
                    nums[i] = 1
        return deleted