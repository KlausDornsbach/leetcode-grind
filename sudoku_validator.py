class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            row = []
            col = []
            box = []

            # box check
            box_i, box_j = (i//3)*3, (i%3)*3
            for j in range(9):
                tmp = board[j//3 + box_i][j%3 + box_j]
                if tmp != '.' and tmp in box:
                    return False
                
                box.append(tmp)
            
            # row check
            for j in range(9):
                tmp = board[i][j]
                if tmp != '.' and tmp in row:
                    return False

                row.append(tmp)

            # col check
            for j in range(9):
                tmp = board[j][i]
                if tmp != '.' and tmp in col:
                    return False

                col.append(tmp)

        return True