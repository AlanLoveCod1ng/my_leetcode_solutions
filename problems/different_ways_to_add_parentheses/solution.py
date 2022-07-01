class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.dfs(expression)
    
    def dfs(self, expression):
        digits = ''
        result = []
        operator = False
        for i in range(len(expression)):
            char = expression[i]
            if char == '+' or char == '-' or char == '*':
                operator = True
                operands1 = self.dfs(expression[:i])
                operands2 = self.dfs(expression[i+1:])
                for i in operands1:
                    for j in operands2:
                        if char == '+':
                            result.append(i+j)
                        elif char == '-':
                            result.append(i-j)
                        elif char == '*':
                            result.append(i*j)
            else:
                digits+=char
        if not operator:
            result = [int(digits)]
        return result