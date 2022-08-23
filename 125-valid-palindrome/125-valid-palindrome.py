class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        start = 0
        end = len(s)-1
        while start<=end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True