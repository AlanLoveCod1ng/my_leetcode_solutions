class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(coord):
            stack = [coord]
            visited = set([])
            captured = True
            while stack:
                current = stack.pop()
                if on_boundary(current):
                    return
                if current in visited:
                    continue
                visited.add(current)
                row, col = current
                if board[row-1][col] == 'O':
                    stack.append((row-1,col))
                if board[row][col-1] == 'O':
                    stack.append((row,col-1))
                if board[row+1][col] == 'O':
                    stack.append((row+1,col))
                if board[row][col+1] == 'O':
                    stack.append((row,col+1))
            for coord in visited:
                row,col = coord
                board[row][col] = "X"
                
        def on_boundary(coord):
            row,col = coord
            return row == 0 or row == len(board)-1 or col == 0 or col == len(board[0])-1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                # if it's on the boundary
                if not on_boundary((i,j)) and board[i][j] == 'O':
                    dfs((i,j))