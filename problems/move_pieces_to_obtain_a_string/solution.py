class Solution:
    def canChange(self, start: str, target: str) -> bool:
        leftStart = []
        leftTarget = []
        rightStart = []
        rightTarget = []
        right_left_start = []
        right_left_after = []
        for i in range(len(start)):
            if start[i] == 'L':
                leftStart.append(i)
                right_left_start.append(1)
            elif start[i] == 'R':
                rightStart.append(i)                
                right_left_start.append(2)

                
            if target[i] == 'L':
                leftTarget.append(i)
                right_left_after.append(1)
            elif target[i] == 'R':
                rightTarget.append(i)
                right_left_after.append(2)
            
        if right_left_start !=right_left_after:
            return False
        for i in range(len(leftStart)):
            if leftStart[i]<leftTarget[i]:
                return False
        for i in range(len(rightStart)):
            if rightStart[i]>rightTarget[i]:
                return False
        return True