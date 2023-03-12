class Solution:
    def closedIsland(self, grid) -> int:
        grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
        def dfs(grid, x, y, m, n):
            if grid[x][y]==1:
                return
            grid[x][y] = 1
            points = [(0, 1), (0, -1), (-1,0), (1, 0)]
            for point in points:
                dx, dy = point
                if 0<=x+dx<m and 0<=y+dy<n:
                    if grid[dx+x][dy+y]==0:
                        dfs(grid, x+dx, y+dy, m, n)

        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            dfs(grid, i,0, m, n)
            dfs(grid, i, n-1, m, n)
        for j in range(n):
            dfs(grid, 0, j, m ,n)
            dfs(grid, m-1, j, m, n)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    dfs(grid, i,j, m, n)
                    count += 1
        return count

a = Solution()
grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]

a.closedIsland(grid)