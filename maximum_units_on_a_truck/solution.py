import heapq
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        hashtable = {}
        heap = []
        totalUnits = 0
        numSet = set([])
        for i in boxTypes:
            hashtable[i[1]] = hashtable.get(i[1],0)+i[0]
            if i[1] in numSet:
                continue
            heapq.heappush(heap, -i[1])
            numSet.add(i[1])
        while len(heap) != 0 and truckSize > 0:
            currentUnit = -heapq.heappop(heap)
            numOfBox = min(truckSize, hashtable[currentUnit])
            totalUnits += numOfBox*currentUnit
            truckSize -=numOfBox
        return totalUnits