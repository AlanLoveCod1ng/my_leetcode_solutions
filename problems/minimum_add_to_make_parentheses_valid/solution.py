class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        num = 0
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if len(stack) != 0:
                    stack.pop()
                else:
                    num+=1
        num+=len(stack)
        return num