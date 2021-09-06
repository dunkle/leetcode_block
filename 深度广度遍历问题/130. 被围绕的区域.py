class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        直接从边缘开始，以“O” 为起始点，往外扩展找出所有与边缘相连的点。四条边，dfs
        剩下的所有的“O”则是被包围的“O”
        '''
        if not  board:
            return
        m = len(board)
        n = len(board[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        def isvalue(x,y):
            if 0<=x<m and 0<=y<n:
                return True
            return False
        def dfs(board, visited, i, j):
            visited[i][j]=1
            steps = ([-1,0], [1,0], [0,1],[0,-1])
            for step in steps:
                x = i+step[0]
                y = j+step[1]
                if isvalue(x,y) and board[x][y]=='O' and visited[x][y]==0:
                    dfs(board, visited, x, y)

        for i in range(m):
            if visited[i][0]==0 and board[i][0]=='O':
                dfs(board, visited, i, 0)
            if visited[i][n-1]==0 and board[i][n-1]=='O':
                dfs(board, visited, i, n-1)
        for j in range(n):
            if visited[0][j]==0 and board[0][j]=='O':
                dfs(board, visited, 0, j)
            if visited[m-1][j]==0 and board[m-1][j]=='O':
                dfs(board, visited, m-1, j)
        for i in range(1,m-1):
            for j in range(1,n-1):
                if visited[i][j]==0 and board[i][j]=='O':
                    board[i][j] = 'X'
        print(board)

a = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["X"]]
board =  [["O","O"],["O","O"]]
board = [["O","O","O"],["O","O","O"],["O","O","O"]]
a.solve(board)