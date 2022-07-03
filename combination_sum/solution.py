class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.result = []
        self.backtrace([],target,0)
        return self.result
    def backtrace(self, current, left, startIndex):
        if left == 0:
            self.result.append(current)
            return
        for i in range(startIndex,len(self.candidates)):
            if self.candidates[i] <= left:
                temp = current.copy()
                temp.append(self.candidates[i])
                self.backtrace(temp,left-self.candidates[i],i)
            else:
                break