class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for i in range(len(strs)):
            counts = [0]*26
            for j in strs[i]:
                counts[ord(j)-ord('a')] += 1
            counts = [str(a) for a in counts]
            counts = " ".join(counts)
            temp_list = hashtable.get(counts,[])
            temp_list.append(strs[i])
            hashtable[counts] = temp_list
        ans = []
        for i in hashtable:
            ans.append(hashtable[i])
        return ans