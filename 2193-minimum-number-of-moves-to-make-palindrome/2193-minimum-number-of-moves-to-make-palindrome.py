class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        res = 0
        while len(s) > 2:
            first = s[0]
            index = len(s)-1
            count = 0
            while s[index] != first:
                index -= 1
                count += 1
            if index == 0:
                res += int(len(s)/2)
            else:
                res += count
            s = s[1:index] + s[index+1:]
        return res
    
#     def minMovesToMakePalindrome(self, s: str) -> int:
#         res = 0
#         s = s[::-1]
#         s_list = list(s)
#         while len(s) > 2:
#             first = s[-1]
#             index = 0
#             count = 0
#             while s[index] != first:
#                 index += 1
#                 count += 1
#             res += count
#             s = s[:index] + s[index+1:len(s)-1]
            
#         return res
    
#     def minMovesToMakePalindrome(self, s):
#         s = s[::-1]
#         s_list = list(s)
#         res = 0
#         while s:
#             i = s.index(s[-1])
#             if i == len(s) - 1:
#                 res += i / 2
#             else:
#                 res += i
#                 s.pop(i)
#             s.pop()
#         return res