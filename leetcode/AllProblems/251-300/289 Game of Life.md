# 289. Game of Life

![image-20200410145504502](../../.assert/image-20200410145504502.png)

~~~python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_neighbors(x, y, board):
            dx = [1,1,1,0,0,-1,-1,-1]
            dy = [1,0,-1,1,-1,1,0,-1]
            neighbors = []
            
            
            for i in range(8):
                nx, ny = x+dx[i], y+dy[i]
                if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[x]):
                    neighbors.append(0)
                else:
                    neighbors.append(board[nx][ny])
            
            return neighbors
        next_state = [list(c) for c in board]
        for i in range(len(board)):
            for j in range(len(board[i])):
                neightbors = get_neighbors(i, j, board)
                live_cell = sum(neightbors)
                if board[i][j] == 1:
                    if live_cell < 2:
                        next_state[i][j] = 0
                    elif live_cell == 2 or live_cell == 3:
                        next_state[i][j] = 1
                    elif live_cell > 3:
                        next_state[i][j] = 0
                else:
                    if live_cell == 3:
                        next_state[i][j] = 1
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = next_state[i][j]
~~~

时间空间复杂度均为O(m*n)

## 解2

可以不用创建一个拷贝，用-1表示1->0,2表示0->1

~~~python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_neighbors(x, y, board):
            dx = [1,1,1,0,0,-1,-1,-1]
            dy = [1,0,-1,1,-1,1,0,-1]
            neighbors_live = 0
            
            
            for i in range(8):
                nx, ny = x+dx[i], y+dy[i]
                if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[x]):
                    continue
                else:
                    if board[nx][ny] == 1 or board[nx][ny] == -1:
                        neighbors_live += 1
            
            return neighbors_live
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                live_cell = get_neighbors(i, j, board)
                if board[i][j] == 1:
                    if live_cell < 2 or live_cell > 3:
                        board[i][j] = -1
                else:
                    if live_cell == 3:
                        board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
~~~

