'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    # 从头开始遍历所有
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        self.res =0
        dpivot = []
        def isval(x,y):
            if 0<=x<m and 0<=y<n:
                return True
            return False
        def dfs(x,y):
            # 深搜 终止，达到目标点，并且目标点位置为可达点
            if (x,y)==(m-1,n-1):
                self.res+=1
                return
            if x==m or y==n:
                return
            # 只能向下或者向右
            steps = [(1,0), (0,1)]
            for step in steps:
                x1 = step[0]+x
                y1 = step[1]+y
                # 向下或者向右的点存在，并且 没有障碍点
                if isval(x1,y1) and obstacleGrid[x1][y1]==0:
                    dfs(x1,y1)
            return
        # 需要判断起点为0 尾部点为0 表示可达
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return self.res
        dfs(0,0)
        return self.res

    def uniquePathsWithObstacles_1(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = 0
        # 到 位置 i,j包含很多重复遍历的路径点，通过记录可以直接获得该值
        dpivot = {}

        # 判断是否超界限
        def isval(x,y):
            if 0<=x<m and 0<=y<n:
                return True
            return False
        # 不断递归，代表到位置 x,y 的位置有多少种可能路径
        def dfs(x,y):
            # 如果遍历到起点位置，代表找到一条路径
            if (x,y)==(0,0):
                return 1
            res = 0

            # 只能向上或者向左递推
            steps = [(-1,0), (0,-1)]
            for step in steps:
                x1 = step[0]+x
                y1 = step[1]+y
                # 新点，如果在字典里，代表可以直接取到。
                if (x1,y1) in dpivot:
                    res+=dpivot[(x1,y1)]
                    continue
                else:
                    # 新点没有超界限并且新点无障碍
                    if isval(x1,y1) and obstacleGrid[x1][y1]==0:
                        res+=dfs(x1,y1)
            #到位置x,y 处点的可能路径，是 从该点上方和左方来的路径线路之和
            dpivot[(x,y)] = res
            return res
        # 需要判断起点为0 尾部点为0 表示可达
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return res
        res = dfs(m-1,n-1)
        return res

a = Solution()

obstacleGrid = [[0,1],[0,0]]
obstacleGrid = [[1]]
obstacleGrid = [[1]]
obstacleGrid = [[1,0]]
obstacleGrid = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],
                [1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],
                [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],
                [0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],
                [1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],
                [0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
                [0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
                [0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
                [1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]
# obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# obstacleGrid = [[0,1],[0,0]]
# obstacleGrid = [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]
res = a.uniquePathsWithObstacles_1(obstacleGrid)
print(res)
