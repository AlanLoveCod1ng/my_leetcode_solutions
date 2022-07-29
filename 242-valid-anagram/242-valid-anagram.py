class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table1 = {}
        table2 = {}
        for i in range(len(s)):
            table1[s[i]] = table1.get(s[i],0)+1
            table2[t[i]] = table2.get(t[i],0)+1
        if len(table1.keys()) != len(table2.keys()):
            return False
        for i in table1:
            if table1.get(i,0) != table2.get(i,0):
                return False

        return True