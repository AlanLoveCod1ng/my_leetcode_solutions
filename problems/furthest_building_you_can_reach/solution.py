import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        i = 0
        while i < len(heights)-1 :
            if heights[i+1]<=heights[i]:
                i+=1
                continue
            heightDiff = heights[i+1]-heights[i]
            heapq.heappush(heap,-heightDiff)
            bricks -= heightDiff
            i+=1
            if bricks < 0:
                if ladders > 0:
                    poppedDiff = -heapq.heappop(heap)
                    bricks+=poppedDiff
                    ladders -= 1
                else:
                    i-=1
                    break
        return i
                    