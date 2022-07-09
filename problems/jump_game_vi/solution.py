from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dq = deque([])
        dp = [-math.inf]*len(nums)
        for i in range(len(nums)):
            while len(dq) != 0 and dq[0] < i-k:
                dq.popleft()
            if len(dq) == 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[dq[0]] + nums[i]
            while len(dq)!=0 and dp[dq[-1]] < dp[i]:
                dq.pop()
            dq.append(i)
        return dp[-1]
        