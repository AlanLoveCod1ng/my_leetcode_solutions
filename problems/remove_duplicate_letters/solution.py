class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        record = [0]*26
        pos = 0
        for i in s:
            record[ord(i)-ord("a")]+=1
        for i in range(len(s)):
            if ord(s[i])<ord(s[pos]):
                pos = i
            record[ord(s[i])-ord("a")]-=1
            if record[ord(s[i])-ord("a")] == 0:
                break
        if len(s) == 0:
            return ""
        else:
            return s[pos] + self.removeDuplicateLetters(s[pos + 1:].replace(s[pos], ""))
        