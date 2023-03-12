给定一个可解的数独，求其解

利用回溯法，向'.'的位置放值，放该值时判断该值是否有效，需要判断：

1. 当前行是否有该值
2. 当前列是否有该值
3. 当前位置所处的区块内是否有该值

如果上述条件都满足，则填入，然后寻找下一个'.'，直到所有的位置都填满

~~~python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 找到一个未填数的位置
        def find_unsigned(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return i, j
            return -1, -1
        # 不断填表
        def dfs(board):
            x, y = find_unsigned(board)
            if x == -1 and y == -1:
                return True
            
            for i in map(str, range(1, 10)):
                if is_safe(board, x, y, i):
                    board[x][y] = i
                    if dfs(board):
                        return True
                    board[x][y] = '.'
        # 判断在(x,y)位置处填ch是否有效  
        def is_safe(board, x, y, ch):
            safe_row = all([board[_][y] != ch for _ in range(9)])
            safe_col = all([board[x][_] != ch for _ in range(9)])
            safe_square = all([board[i][j] != ch for i in get_range(x) for j in get_range(y)])
            return safe_row and safe_col and safe_square
        # 获取x位置的所处的square范围
        def get_range(x):
            x-=x%3
            return range(x, x+3)
        
        
        dfs(board)
~~~

