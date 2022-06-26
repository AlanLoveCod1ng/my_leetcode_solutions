class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum = 0
        rightSum = 0
        result = 0
        for i in range(k):
            leftSum+=cardPoints[i]
        result = leftSum
        for i in range(k):
            rightSum += cardPoints[len(cardPoints)-1-i]
            leftSum -= cardPoints[k-1-i]
            result = max(result,leftSum+rightSum)
        return result