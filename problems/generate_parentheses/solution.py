class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.backTracing("",0,n)
        return self.result
        
    def backTracing(self, s,inStack,left):
        if inStack == 0 and left == 0:
            self.result.append(s)
            return
        if inStack != 0:
            self.backTracing(s+")",inStack-1,left)
        if left != 0:
            self.backTracing(s+"(", inStack+1, left-1)