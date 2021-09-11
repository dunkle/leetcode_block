class Solution:
    def isValidSudoku(self, board):
        # 判断行有效
        def row_isval(board):
            m = len(board)
            dictmap = {}
            for i in range(m):
                for j in range(len(board[0])):
                    if board[i][j]==".":
                        continue
                    if board[i][j] in dictmap:
                        return False
                    else:
                        dictmap[board[i][j]] = 1
                dictmap = {}
            return True
        def col_isval(board):
            n = len(board[0])
            dictmap = {}
            for j in range(n):
                for i in range(len(board)):
                    if board[i][j]==".":
                        continue
                    if board[i][j] in dictmap:
                        return False
                    else:
                        dictmap[board[i][j]] = 1
                dictmap = {}
            return True
        def nineblock_val(board):
            m = len(board)
            n = len(board[0])
            i, j = 0, 0
            while i<3:
                while j<3:
                    dictmap ={}
                    for r in range(i*3, i*3+3):
                        for t in range(j*3, j*3+3):
                            if board[r][t]==".":
                                continue
                            if board[r][t] in dictmap:
                                return False
                            else:
                                dictmap[board[r][t]] = 1
                    j+=1
                j = 0
                i+=1
            return True
        return row_isval(board) and col_isval(board) and nineblock_val(board)

a = Solution()
board = [[".",".",".",".",".",".","5",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         ["9","3",".",".","2",".","4",".","."],
         [".",".","7",".",".",".","3",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".","3","4",".",".",".","."],
         [".",".",".",".",".","3",".",".","."],
         [".",".",".",".",".","5","2",".","."]]
res = a.isValidSudoku(board)
print(res)