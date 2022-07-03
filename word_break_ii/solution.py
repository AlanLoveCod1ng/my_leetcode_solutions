class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        dp = [False]*(len(s)+1)
        dpStr = [[]for _ in range(len(s)+1)]
        dpStr[0] = ['']
        dp[0] = True
        for endIndex in range(1,len(dp)):
            for startIndex in range(endIndex,0,-1):
                temp = s[startIndex-1:endIndex] in wordset and dp[startIndex-1]
                if temp:
                    dp[endIndex] = True
                    for prev in dpStr[startIndex-1]:
                        dpStr[endIndex].append((prev+' '+s[startIndex-1:endIndex]).strip())
        return dpStr[-1]
        