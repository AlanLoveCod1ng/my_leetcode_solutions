import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        max_value = 0
        ans = math.inf
        #pretreatment: divide number until it turn into an odd number
        for i in range(len(nums)):
            a = nums[i]
            heapq.heappush(heap,[a/(a & -a), a])
            max_value = max(max_value, a/(a & -a))
        while len(heap) == len(nums):
            a, a0 = heapq.heappop(heap)
            ans = min(max_value - a, ans)
            if a % 2 == 1 or a < a0:
                heapq.heappush(heap,[a*2,a0])
                max_value = max(a*2, max_value)
        return int(ans)