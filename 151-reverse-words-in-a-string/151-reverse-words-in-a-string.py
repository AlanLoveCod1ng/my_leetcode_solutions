class Solution:
    def reverseWords(self, s: str) -> str:
        #Time O(N) Space O(1)
        
        words = []
        #two pointers mark the start and end of a word
        start = -1
        end = start
        #iterate the string
        for i in range(len(s)):
            # current char is space
            #reset start and end
            if s[i] == ' ':
                # first space after a word
                if start != -1:
                    words.append(s[start:end+1])
                start = -1
                end = -1
                continue
            
            #a new word
            if start == -1:
                start = i
            #update end
            end = i
        if start != -1:
            words.append(s[start:end+1])
        words.reverse()
        return " ".join(words)
            