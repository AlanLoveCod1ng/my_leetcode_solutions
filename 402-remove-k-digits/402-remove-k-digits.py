class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #monotonic stack
        #time: O(N) space: O(N)
        
        #boundary k >= len(num)
        if k >= len(num):
            return '0'
        
        stack = [] # increasing stack
        for i in range(len(num)):
            if len(stack) == 0:
                stack.append(num[i])
                continue
            # pop element at top which is larger than current
            # to keep monotonic
            current = num[i]
            while stack and int(stack[-1]) > int(current):
                if k > 0:
                    stack.pop()
                    k -= 1
                else:
                    break
            # after this loop, stack might be empty
            # or the top of the stack is less than current
            stack.append(current)
        # boundary case: num is increasing order
        # e.g. "123456" k = 2 stack would not pop any element in this case
        while k > 0:
            stack.pop()
            k -= 1
        res = "".join(stack)
        # res first digit might be zero 02 -> 2 0->0
        start = 0
        for i in range(len(res)):
            if res[i] == '0':
                start = i+1
            else:
                break
        if start >=len(res):
            return '0'
        return res[start:]