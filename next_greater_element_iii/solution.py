class Solution:
    def nextGreaterElement(self, n: int) -> int:
        maxValue = 2147483647
        digits = []
        temp = n
        while temp!=0:
            digits.append(temp%10)
            temp=int(temp/10)
        increasing = True
        for i in range(1,len(digits),1):
            if digits[i]<digits[i-1]:
                increasing = False
                break
        if increasing:
            return -1
        for i in range(len(digits)):
            ancestors = digits[:i]
            found = False
            for j in range(len(ancestors)):
                if ancestors[j]>digits[i]:
                    found = True
                    temp = digits[i]
                    digits[i] = ancestors[j]
                    ancestors[j] = temp
                    for z in range(i):
                        digits[z] = ancestors[i-1-z]
                    break
            if found:
                break
        result = 0
        for i in range(len(digits)):
            result+=digits[i]*(10**i)
        if result>maxValue:
            return -1
        return result