import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap,-i)
        result = 0
        for j in range(k):
            result = -heapq.heappop(heap)
        return result
            