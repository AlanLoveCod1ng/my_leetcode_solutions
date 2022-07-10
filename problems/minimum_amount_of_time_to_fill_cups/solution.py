class Solution:
    def fillCups(self, amount: List[int]) -> int:
        output = 0
        while True:
            amount = sorted(amount)
            if amount[2] == 0:
                return output
            amount[2] -= 1
            if amount[1] !=0:
                amount[1] -= 1
            output+=1
        return output