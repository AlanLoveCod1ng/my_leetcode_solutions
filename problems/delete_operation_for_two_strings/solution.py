class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word2))]for j in range(len(word1))]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1]
                    if word1[i] == word2[j]:
                        dp[i][j] = 1
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i-1][j]
                    if word1[i] == word2[j]:
                        dp[i][j] = 1
                elif i ==0 and j == 0:
                    if word1[i] == word2[j]:
                        dp[i][j] = 1
                else:
                    if word1[i]==word2[j]:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return len(word1)+len(word2)-2*dp[i][j]