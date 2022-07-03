class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        prev = 0
        bestHeight = 0
        modulo = 10**9+7
        horizontalCuts.append(h)
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts.append(w)
        verticalCuts = sorted(verticalCuts)
        for i in range(len(horizontalCuts)):
            bestHeight = max(horizontalCuts[i]-prev, bestHeight)
            prev = horizontalCuts[i]
        prev = 0
        bestWidth = 0
        for i in range(len(verticalCuts)):
            bestWidth = max(verticalCuts[i] - prev, bestWidth)
            prev = verticalCuts[i]
        return bestWidth * bestHeight % modulo
            