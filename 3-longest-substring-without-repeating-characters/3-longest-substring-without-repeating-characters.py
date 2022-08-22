class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        res = 0
        hashtable = {}
        for i in range(len(s)):
            current_char = s[i]
            hashtable[current_char] = hashtable.get(current_char, 0)+1
            if hashtable[current_char] == 2:
                while hashtable[s[start]] != 2:
                    hashtable[s[start]] -= 1
                    start += 1
                hashtable[s[start]] -= 1
                start += 1
            res = max(res, i-start+1)
        return res