class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        hashtable = {}
        res = 0
        for i in range(len(s)):
            maxlen = 0
            currentChar = s[i]
            for i in range(k+1):
                larger = hashtable.get(chr(ord(currentChar)+i),0)+1
                lower = hashtable.get(chr(ord(currentChar)-i),0) +1
                maxlen = max(maxlen,larger)
                maxlen = max(maxlen,lower)
            hashtable[currentChar] = maxlen
            res = max(maxlen,res)
        return res