import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        cmpa = lambda x,y: 1 if x+y > y+x else -1 if x+y<y+x else 0
        nums_s = list(map(str,nums))
        nums_s.sort(key=functools.cmp_to_key(cmpa), reverse = True)
        return str(int("".join(nums_s)))