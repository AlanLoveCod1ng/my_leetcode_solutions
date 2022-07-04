class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyLeft = [1]*len(ratings)
        candyRight = [1]*len(ratings)
        candy = [1]*len(ratings)
        for i in range(len(ratings)):
            if i != 0:
                if ratings[i] > ratings[i-1] and candyLeft[i]<=candyLeft[i-1]:
                    candyLeft[i] = candyLeft[i-1]+1
            if i != len(ratings)-1:
                if ratings[i] > ratings[i+1] and candyLeft[i]<=candyLeft[i+1]:
                    candyLeft[i] = candyLeft[i+1]+1
                    
        for i in range(len(ratings)-1,-1,-1):
            if i != 0:
                if ratings[i] > ratings[i-1] and candyRight[i]<=candyRight[i-1]:
                    candyRight[i] = candyRight[i-1]+1
            if i != len(ratings)-1:
                if ratings[i] > ratings[i+1] and candyRight[i]<=candyRight[i+1]:
                    candyRight[i] = candyRight[i+1]+1
        
        for i in range(len(ratings)):
            candy[i] = max(candyLeft[i],candyRight[i])
        return sum(candy)