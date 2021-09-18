'''
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        # 直接为空，返回0
        if m==0:
            return 0
        # 判断是否越界
        def is_val(i, j):
            if 0<=i<m and 0<=j<n:
                return True
            return False
        # dfs搜索一下与之相连的岛屿
        def recur(i,j):
            # 此处返回 岛屿面积0，作为终止条件
            if not is_val(i,j) or grid[i][j]==0:
                return 0
            grid[i][j] = 0
            steps = [(-1,0), (0, -1), (0,1), (1,0)]
            ans = 1
            # 可遍历的岛屿，此处没有做越界判断，而是直接递归节点与 终止条件对应
            for step in steps:
                x = i+step[0]
                y = j+step[1]
                ans = recur(x,y) +ans
            # 返回的是当前节点可达的岛屿节点
            return ans
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    res = max(res,recur(i, j))
        return res