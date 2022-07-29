class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        unit = 1
        while left != right:
            left = left >> 1
            right = right >> 1
            unit = unit << 1
        return left*unit
                
