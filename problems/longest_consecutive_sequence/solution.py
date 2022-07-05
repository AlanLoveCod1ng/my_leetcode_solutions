class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_streak = 0
        for i in nums:
            if i-1 not in nums:
                current = i
                current_streak = 1
                while current + 1 in nums:
                    current_streak += 1
                    current = current+1
                longest_streak = max(longest_streak,current_streak)
        return longest_streak