class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == "":
            return s2 == s3
        if s2 == "":
            return s1 == s3
        if s3 == "":
            return s1 == s2 and s1 == ""
        if len(s3) != len(s1)+len(s2):
            return False
        dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(1,len(dp)):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1,len(dp[0])):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                a = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                b = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[i][j]
        
                