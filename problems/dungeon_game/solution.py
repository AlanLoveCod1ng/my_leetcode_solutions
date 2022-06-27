class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dpBot = [[float('inf')]*len(dungeon[0]) for _ in range(len(dungeon))]
        dpRight = [[float('inf')]*len(dungeon[0]) for _ in range(len(dungeon))]
        dpBot[-1][-1] = 1+abs(dungeon[-1][-1]) if dungeon[-1][-1] <= 0 else 1
        dpRight[-1][-1] = dpBot[-1][-1]
        height = len(dungeon)
        width = len(dungeon[0])
        for i in range(width-2, -1,-1):
            dpRight[height-1][i] = max(dpRight[height-1][i+1]-dungeon[height-1][i], 1)
        for i in range(height-2, -1, -1):
            dpBot[i][width-1] = max(dpBot[i+1][width-1]-dungeon[i][width-1], 1)
        for i in range(height-2,-1,-1):
            for j in range(width-2, -1, -1):
                dpRight[i][j] = max(min(dpRight[i][j+1],dpBot[i][j+1])-dungeon[i][j],1)
                dpBot[i][j] = max(min(dpRight[i+1][j],dpBot[i+1][j])-dungeon[i][j],1)
        return min(dpRight[0][0],dpBot[0][0])