class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hashtable = {}
        length = len(arr)
        for i in arr:
            hashtable[i] = hashtable.get(i,0) + 1
        heap = []
        for i in hashtable:
            heapq.heappush(heap,-hashtable[i])
        removed = 0
        res = 0
        while removed < length/2:
            removed += -heapq.heappop(heap)
            res += 1
        return res