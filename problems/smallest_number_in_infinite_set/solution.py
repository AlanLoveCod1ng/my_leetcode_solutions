
class SmallestInfiniteSet:
    
    def __init__(self):
        self.removed = set([])    
        self.min = 1
    def popSmallest(self) -> int:
        record = self.min
        self.removed.add(self.min)
        while self.min in self.removed:
            self.min+=1
        return record
    def addBack(self, num: int) -> None:
        self.removed.discard(num)
        self.min = min(num,self.min)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)