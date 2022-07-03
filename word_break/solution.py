class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for endIndex in range(1,len(dp)):
            for startIndex in range(endIndex,0,-1):
                dp[endIndex] = s[startIndex-1:endIndex] in wordset and dp[startIndex-1]
                if dp[endIndex]:
                    break
        return dp[-1]