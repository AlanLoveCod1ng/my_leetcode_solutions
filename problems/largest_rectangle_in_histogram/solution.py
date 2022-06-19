class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [-1]
        for i in range(len(heights)):
            if len(stack) == 1:
                stack.append(i)
                continue
            if heights[stack[-1]] < heights[i]:
                stack.append(i)
            else:
                while(heights[stack[-1]]>=heights[i] and len(stack)>1):
                    currentArea = heights[stack[-1]]*(i-stack[-2]-1)
                    maxArea = max(currentArea, maxArea)
                    stack.pop()
                stack.append(i)
        while len(stack)>1:
            currentArea = heights[stack[-1]]*(len(heights)-1-stack[-2])
            maxArea = max(currentArea, maxArea)
            stack.pop()
        return maxArea
                