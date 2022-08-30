class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # time complexity: O(m*n + L) space O(m*n)
        
        self.queue = deque([])
        self.visited = set([])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.queue.append((i,j,0))
                    if self.bfs(word,board):
                        return True
                    self.queue.pop()
        return False
    def bfs(self,word,board):
            coordinate = self.queue.popleft()
            cur_row, cur_col, index = coordinate
            if (cur_row,cur_col) in self.visited:
                self.queue.appendleft(coordinate)
                return False
            self.visited.add((cur_row,cur_col))
            if index == len(word)-1:
                return True
            if cur_row - 1 >= 0 and board[cur_row-1][cur_col] == word[index+1]:
                self.queue.append((cur_row-1,cur_col,index+1))
                if self.bfs(word,board):
                    return True
                self.queue.pop()
            if cur_row + 1 < len(board) and board[cur_row+1][cur_col] == word[index+1]:
                self.queue.append((cur_row+1,cur_col,index+1))
                if self.bfs(word,board):
                    return True
                self.queue.pop()
            if cur_col - 1 >= 0 and board[cur_row][cur_col-1] == word[index+1]:
                self.queue.append((cur_row,cur_col-1,index+1))
                if self.bfs(word,board):
                    return True
                self.queue.pop()
            if cur_col + 1 < len(board[0]) and board[cur_row][cur_col+1] == word[index+1]:
                self.queue.append((cur_row,cur_col+1,index+1))
                if self.bfs(word,board):
                    return True
                self.queue.pop()
            self.queue.appendleft(coordinate)
            self.visited.remove((cur_row,cur_col))
            return False