import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a != 0:
            heapq.heappush(heap,[-a,'a'])
        if b != 0:
            heapq.heappush(heap,[-b,'b'])
        if c != 0:
            heapq.heappush(heap,[-c,'c'])
        s = ""
        repeat = {'a':0,'b':0,'c':0}
        while len(heap) != 0:
            amount, letter = heapq.heappop(heap)
            if repeat[letter] == 2:
                if len(heap) == 0:
                    break
                amount1,letter1 = heapq.heappop(heap)
                heapq.heappush(heap,[amount,letter])
                amount = amount1
                letter = letter1
            amount = -amount
            s += letter
            amount -= 1
            occur = repeat[letter]
            for i in repeat:
                repeat[i] = 0
            repeat[letter] = occur + 1
            if amount:
                heapq.heappush(heap,[-amount,letter])
        return s