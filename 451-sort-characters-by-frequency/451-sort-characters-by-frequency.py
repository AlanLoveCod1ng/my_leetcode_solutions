class Solution:
    def frequencySort(self, s: str) -> str:
        maxFrequence = 0
        hashtable = {}
        for i in range(len(s)):
            hashtable[s[i]] = hashtable.get(s[i],0)+1
            maxFrequence = max(maxFrequence, hashtable[s[i]])
        buckets = [[] for _ in range(maxFrequence+1)]
        for i in hashtable:
            current_char = i
            current_frequence = hashtable[i]
            buckets[current_frequence].append(current_char)
        res = []
        for i in range(len(buckets)-1,-1,-1):
            for char in buckets[i]:
                for j in range(i):
                    res.append(char)
        return "".join(res)
        