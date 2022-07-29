class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        temp = [Interval(a) for a in intervals]
        temp = sorted(temp)
        result = [temp[0].list]
        for i in range(1,len(temp)):
            if result[-1][1] >= temp[i].list[0]:
                result[-1][1] = max(temp[i].list[1],result[-1][1])
            else:
                result.append(temp[i].list)
        return result
        
class Interval:
    def __init__(self, interval):
        self.list = interval
        self.start = interval[0]
        self.end = interval[1]
    def __lt__(self, another):
        if self.start == another.start:
            return self.end < another.end
        return self.start<another.start