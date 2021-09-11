class Solution:
    def largestIsland(self, grid) -> int:
        # grid = [[1, 1], [1, 1]]
        # grid = [[1, 1], [1, 0]]
        m = len(grid)
        n = len(grid[0])
        root = [[0 for i in range(n)] for j in range(m)]
        area = {}

        def dfs(grid, root, x, y, now):
            if grid[x][y]==1 and root[x][y]==0:
                root[x][y] = now
                nowarea = 1
                steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                for step in steps:
                    dx, dy = step
                    if 0<= dx+x<m and 0<= dy+y <n:
                        nowarea += dfs(grid, root, x+dx, y+dy, now)
                return nowarea
            else:
                return 0

        def getmaxarea(grid, root, x, y, area):
            steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            rootindex = set()
            maxarea = 0
            for i, step in enumerate(steps):
                dx, dy = step
                if 0<= dx+x<m and 0<= dy+y <n:
                    if grid[x+dx][y+dy]!=0:
                        rootindex.add(root[x+dx][y+dy])
            for i in rootindex:
                maxarea+=area[i]
            return maxarea+1

        now = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and root[i][j]==0:
                    area[now] = dfs(grid, root, i, j, now)
                    now +=1
        print(area)
        if len(area)==0:
            return 0
        results = max(1, max(area.values()))
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    results = max(results, getmaxarea(grid, root, i, j, area))
        return results
        # print(area)
        # print(root)

# grid = [[1, 1], [1, 0]]
grid = [[1, 0], [0, 1]]
# grid = [[1, 1], [1, 1]]
grid = [[0]]
grid = [[]]

a = Solution()
results = a.largestIsland(grid)
print(results)


