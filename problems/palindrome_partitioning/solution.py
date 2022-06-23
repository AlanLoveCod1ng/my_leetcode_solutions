class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.dfs(s, 0,[])
        return self.result
    def dfs(self, s, start,current):
        if start == len(s):
            self.result.append(current)
            return
        length = 1
        while start+length <= len(s):
            currentList = current.copy()
            if self.isPalindrome(s[start:start+length]):
                currentList.append(s[start:start+length])
                self.dfs(s,start+length,currentList)
            length +=1
    def isPalindrome(self, s):
        i = 0
        j = len(s)-1
        while i<j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True