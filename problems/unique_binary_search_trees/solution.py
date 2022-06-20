class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3,n+1):
            for j in range(i, 0, -1):
                left = j-1
                right = i-j
                dp[i]+=dp[left]*dp[right]
        return dp[-1]