import functools
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        comp = lambda x,y : 1 if x[0]>y[0] else -1 if x[0]<y[0] else 0
        intervals = sorted(intervals,key = functools.cmp_to_key(comp))
        room = []
        maxNum = 0
        currentTime = 0
        for interval in intervals:
            timeInteval = interval[0] - currentTime
            currentTime = interval[0]
            room = [a-timeInteval for a in room if a-timeInteval>0]
            room.append(interval[1]-interval[0])
            maxNum = max(maxNum,len(room))
        return maxNum
            