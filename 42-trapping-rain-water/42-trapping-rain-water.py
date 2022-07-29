class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        for i in range(len(height)):
            while len(stack)>0 and height[stack[-1]] < height[i]:
                prev = height[stack.pop()]
                if len(stack) == 0:
                    break
                left_bound_index = stack[-1]
                distance = i - left_bound_index - 1
                water = (min(height[i],height[left_bound_index])-prev)*distance
                result += water        
            stack.append(i)
        return result