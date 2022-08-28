class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # start with first row
        for col in range(len(mat[0])):
            temp = []
            row = 0
            cur_row = row
            cur_col = col
            while cur_row < len(mat) and cur_col < len(mat[0]):
                temp.append(mat[cur_row][cur_col])
                cur_row += 1
                cur_col += 1
            temp.sort()
            cur_row = row
            cur_col = col
            index = 0
            while cur_row < len(mat) and cur_col < len(mat[0]):
                mat[cur_row][cur_col] = temp[index]
                index += 1
                cur_row += 1
                cur_col += 1
        for row in range(1,len(mat)):
            temp = []
            col = 0
            cur_row = row
            cur_col = col
            while cur_row < len(mat) and cur_col < len(mat[0]):
                temp.append(mat[cur_row][cur_col])
                cur_row += 1
                cur_col += 1
            temp.sort()
            cur_row = row
            cur_col = col
            index = 0
            while cur_row < len(mat) and cur_col < len(mat[0]):
                mat[cur_row][cur_col] = temp[index]
                index += 1
                cur_row += 1
                cur_col += 1
        return mat