class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i < len(s)-1:
                if s[i] == s[i+1]:
                    dp[i][i+1] = True
        length = 2
        while length < len(s):
            startIndex = 0
            while startIndex+length<len(s):
                dp[startIndex][startIndex+length] = s[startIndex] == s[startIndex+length] and dp[startIndex+1][startIndex+length-1]
                startIndex+=1
            length+=1
        self.dp = dp
        self.result = []
        self.dfs(s, 0,[])
        return self.result
    def dfs(self, s, start,current):
        if start == len(s):
            self.result.append(current)
            return
        length = 0
        while start+length < len(s):
            currentList = current.copy()
            if self.dp[start][start+length]:
                currentList.append(s[start:start+length+1])
                self.dfs(s,start+length+1,currentList)
            length +=1