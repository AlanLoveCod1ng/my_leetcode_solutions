class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        hashtable = {}
        start = 0
        end = 0
        maxLength = 0
        while end < len(s):
            if s[end] not in hashtable:
                hashtable[s[end]] = end
            else:
                newStart = hashtable[s[end]]+1
                while start < newStart:
                    hashtable.pop(s[start],None)
                    start+=1
                hashtable[s[end]] = end
            if end-start > maxLength:
                maxLength = end-start
            end+=1
        return maxLength+1