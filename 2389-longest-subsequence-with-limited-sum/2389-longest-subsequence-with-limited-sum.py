class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(len(queries)):
            length = 0
            sums = 0
            for j in range(len(nums)):
                sums += nums[j]
                if sums > queries[i]:
                    break
                length += 1
            ans.append(length)
        return ans