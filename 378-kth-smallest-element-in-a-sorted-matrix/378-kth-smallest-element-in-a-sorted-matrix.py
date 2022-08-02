import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            heapq.heappush(heap,[matrix[i][0],[i,0]])
        for i in range(k):
            value,pos = heapq.heappop(heap)
            if i == k-1:
                return value
            if pos[1] != len(matrix)-1:
                heapq.heappush(heap,[matrix[pos[0]][pos[1]+1], [pos[0],pos[1]+1]])
        return value
        