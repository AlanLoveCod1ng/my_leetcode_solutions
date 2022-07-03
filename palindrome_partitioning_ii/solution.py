class Solution:
    def minCut(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i < len(s)-1:
                dp[i][i+1] = s[i] == s[i+1]
        length = 2
        while length<len(s):
            startIndex = 0
            while startIndex+length < len(s):
                dp[startIndex][startIndex+length] = s[startIndex] == s[startIndex+length] and dp[startIndex+1][startIndex+length-1]
                startIndex+=1
            length+=1
        dp1 = [0]*len(s)
        dp1[0] = 1
        for endIndex in range(1,len(s)):
            minPar = dp1[endIndex-1]+1
            for startIndex in range(endIndex,-1, -1):
                if startIndex == 0:
                    minPar = 1 if dp[startIndex][endIndex] else minPar
                elif dp[startIndex][endIndex]:
                    minPar = min(minPar, dp1[startIndex-1]+1)
                dp1[endIndex] = minPar
        return dp1[-1]-1
        return self.maxPartition