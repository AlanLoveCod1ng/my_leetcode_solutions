class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp1 = [False]*(len(p)+1)
        dp[0][0] = True
        dp1[0] = True
        for i in range(1,len(dp[0])):
            if p[i-1] == '*':
                dp[0][i] = True
            else:
                break
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == '*':
                    dp[i][j] = dp1[j-1]
                dp1[j] = dp1[j] or dp[i][j]
        return dp[-1][-1]