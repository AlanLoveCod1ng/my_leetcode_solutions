class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        top_max = math.inf
        top_min = -math.inf
        if self.max_heap:
            top_max = -self.max_heap[0]
        if self.min_heap:
            top_min = self.min_heap[0]
        if len(self.min_heap) == len(self.max_heap):
            if num >= top_min:
                heapq.heappush(self.min_heap,num)
            elif num <= top_max:
                heapq.heappush(self.max_heap,-num)
                exchange = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap,exchange)
            else:
                heapq.heappush(self.min_heap,num)
        else:
            if num <= top_min:
                heapq.heappush(self.max_heap,-num)
            else:
                heapq.heappush(self.min_heap, num)
                exchange = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -exchange)
                

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0])/2
        return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()