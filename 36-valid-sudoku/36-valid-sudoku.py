class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set([]) for _ in range(9)]
        cols = [set([]) for _ in range(9)]
        boxes = [set([]) for _ in range(9)]
        for i in range(9):
            for j in range(9):
                current = board[i][j]
                if current == '.':
                    continue
                if current in rows[i]:
                    return False
                rows[i].add(current)
                if current in cols[j]:
                    return False
                cols[j].add(current)
                
                row_matrix = int(i/3)
                col_matrix = int(j/3)
                index_matrix = row_matrix*3+col_matrix
                if current in boxes[index_matrix]:
                    return False
                boxes[index_matrix].add(current)
        return True