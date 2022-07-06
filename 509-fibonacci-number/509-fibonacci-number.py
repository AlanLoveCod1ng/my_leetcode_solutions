class Solution:
    def fib(self, n: int) -> int:
        dp = [0]*(n+1)
        if n == 0:
            return 0
        dp[1] = 1
        for i in range(len(dp)):
            if i > 0:
                dp[i]+=dp[i-1]
            if i > 1:
                dp[i]+=dp[i-2]
        return dp[-1]