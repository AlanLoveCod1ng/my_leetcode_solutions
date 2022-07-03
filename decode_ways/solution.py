class Solution:
    def numDecodings(self, s: str) -> int:
        s = '0'+s
        dp = [0]*len(s)
        dp[0] = 1
        dp[1] += 1 if self.translate(s[1]) else 0
        for i in range(2,len(dp)):
            dp[i] += dp[i-1] if self.translate(s[i]) else 0
            dp[i] += dp[i-2] if self.translate(s[i-1:i+1]) else 0
        return dp[-1]
    def translate(self, s:str):
        if len(s) == 2 and s[0] == '0':
            return False
        if int(s)>26 or int(s) <= 0:
            return False
        return True