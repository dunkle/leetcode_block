'''
给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。

如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1。

 

示例 1：

输入：
grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1
输出：6
解释：
不消除任何障碍的最短路径是 10。
消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

示例 2：

输入：
grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1
输出：-1
解释：
我们至少需要消除两个障碍才能找到这样的路径。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-path-in-a-grid-with-obstacles-elimination
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def shortestPath(self, grid, k: int) -> int:
        R, C = len(grid), len(grid[0])
        if k >= R + C - 2:      #直接贴边走  走了 R + C - 2个步  中间经过 R+C-3个点
            return R + C - 2
        k = min(k, R + C - 3)   #中间最多清楚 R + C - 3个障碍，贴边走就能到
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        visited = [[[False for _ in range(k + 1)] for _ in range(C)] for _ in range(R)]
        queue = []
        visited[0][0][k] = True     #坐标 0,0 还剩k步（还可以开挂k次）可以用
        queue.append([0,0,k])
        level = 1
        while queue:                                #记忆化 BFS 波纹法
            cur_len = len(queue)
            for _ in range(cur_len):                #波纹法
                r,c,remain_step = queue.pop(0)
                for dr,dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        if grid[nr][nc] == 0 and visited[nr][nc][remain_step] == False: #下一步很顺利，是个0，不是障碍
                            if nr == R-1 and nc == C-1:                 #到最右下角终点了
                                return level
                            else:
                                visited[nr][nc][remain_step] = True     #中途普通的位置
                                queue.append([nr, nc, remain_step])
                        elif grid[nr][nc] == 1 and remain_step > 0 and visited[nr][nc][remain_step - 1] == False:   #下一步是个障碍
                            visited[nr][nc][remain_step - 1] = True
                            queue.append([nr, nc, remain_step - 1])
            level += 1

        return -1



a = Solution()
grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
k = 1
res = a.shortestPath(grid, k)
print(res)