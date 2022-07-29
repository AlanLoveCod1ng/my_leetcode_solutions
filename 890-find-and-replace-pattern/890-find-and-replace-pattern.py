class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for i in range(len(words)):
            hashtable1 = {}
            hashtable2 = {}
            word = words[i]
            for j in range(len(word)):
                valid = True
                if word[j] in hashtable1 and pattern[j] in hashtable2:
                    if hashtable1[word[j]] != pattern[j] or hashtable2[pattern[j]] != word[j]:
                        valid = False
                        break
                elif not word[j] in hashtable1 and not pattern[j] in hashtable2:
                    hashtable1[word[j]] = pattern[j]
                    hashtable2[pattern[j]] = word[j]
                else:
                    valid = False
                    break
            if valid:
                result.append(word)
        return result