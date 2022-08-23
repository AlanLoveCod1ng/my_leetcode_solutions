class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #dfs would return the area of this island
        def dfs(i,j):
            # dfs-stack
            stack = [(i,j)]
            area = 0
            while stack:
                i,j = stack.pop()
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                area += 1
                #top
                if i-1 >= 0 and grid[i-1][j] == 1:
                    stack.append((i-1,j))
                #left
                if j-1 >=0 and grid[i][j-1] == 1:
                    stack.append((i,j-1))
                #bot
                if i+1<len(grid) and grid[i+1][j] == 1:
                    stack.append((i+1,j))
                #right
                if j+1<len(grid[0]) and grid[i][j+1] == 1:
                    stack.append((i,j+1))
            return area
        
        res = 0
        visited = set([])
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not (i,j) in visited:
                    res = max(res,dfs(i,j))
        return res