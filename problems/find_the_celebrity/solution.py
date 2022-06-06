# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        possible = 0
        nextOne = 1
        while nextOne < n:
            if knows(possible,nextOne):
                possible = nextOne
            nextOne+=1
        for i in range(n):
            if i==possible:
                continue
            if not knows(i,possible) or knows(possible,i):
                return -1
        return possible