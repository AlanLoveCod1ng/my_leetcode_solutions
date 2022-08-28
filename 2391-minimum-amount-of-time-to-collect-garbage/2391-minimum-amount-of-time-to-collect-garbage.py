class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        M_location = 0
        P_location = 0
        G_location = 0
        res = 0
        distance = [0]*len(garbage)
        for i in range(1,len(distance)):
            distance[i] = travel[i-1]+distance[i-1]
        for i in range(len(garbage)):
            for char in garbage[i]:
                if char == 'M':
                    move_time = distance[i] - distance[M_location]
                    M_location = i
                    res += move_time + 1
                elif char == 'P':
                    move_time = distance[i] - distance[P_location]
                    P_location = i
                    res += move_time + 1
                else:
                    move_time = distance[i] - distance[G_location]
                    G_location = i
                    res += move_time + 1
        return res
                    