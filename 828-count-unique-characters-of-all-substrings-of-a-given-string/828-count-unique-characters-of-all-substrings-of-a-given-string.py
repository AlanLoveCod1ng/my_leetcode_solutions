class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # we may have more than 2 for each char, but we only record index of 2 chars for each.
        dp = [[-1,-1]for _ in range(26)]
        result = 0
        for i in range(len(s)):
            current_char = s[i]
            char_index = ord(current_char)-ord('A')
            result += (dp[char_index][1]-dp[char_index][0]) * (i - dp[char_index][1])
            dp[char_index][0] = dp[char_index][1]
            dp[char_index][1] = i
        for i in range(26):
            if dp[i][1] != -1:
                result+= (len(s) - dp[i][1])*(dp[i][1] - dp[i][0])
        return result