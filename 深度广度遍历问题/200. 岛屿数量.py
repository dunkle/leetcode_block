'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def numIslands(self, grid) -> int:

        m = len(grid)
        n = len(grid[0])
        print(m, n)

        def bfs(grid, i, j):
            steps = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            grid[i][j] = '0'
            for step in steps:
                # print(step)
                x, y = i+step[0], j+step[1]
                if 0<= x <m and 0<= y <n and grid[x][y]=='1':
                    bfs(grid, x, y)
            return

        count = 0
        for i in range(m):
            for j in range(n):
                # print(grid[i][j])
                if grid[i][j]=='1':
                    print("bfs")
                    bfs(grid, i, j)
                    count +=1
        return count

a = Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

print(a.numIslands(grid))