class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.map = {2:['a','b','c'],
                    3:['d','e','f'],
                    4:['g','h','i'],
                    5:['j','k','l'],
                    6:['m','n','o'],
                    7:['p','q','r','s'],
                    8:['t','u','v'],
                    9:['w','x','y','z']}
        self.result = []
        self.dfs('',digits)
        if self.result[0] == "":
            self.result = []
        return self.result
    def dfs(self, currentString, currentDigits):
        if len(currentDigits) == 0:
            self.result.append(currentString)
            return
        possibleChr = self.map[int(currentDigits[0])]
        for i in possibleChr:
            self.dfs(currentString+i,currentDigits[1:])