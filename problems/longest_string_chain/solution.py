class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words,key=len)
        hashtable = {}
        maxRecord = 0
        for i in words:
            maxLen = 0
            for j in range(len(i)):
                temp = i
                maxLen = max(maxLen,hashtable.get(temp[:j]+temp[j+1:],0)+1)
            hashtable[i] = maxLen
            maxRecord = max(maxLen, maxRecord)
        return maxRecord