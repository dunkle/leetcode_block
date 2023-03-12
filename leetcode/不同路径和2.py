class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m==0:
            return 0
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    if m==n==0:
                        dp[i][j] = 1
                    else:
                        a = dp[i-1][j] if i!=0 else 0
                        b = dp[i][j-1] if j!=0 else 0
                        dp[i][j] = a + b
        return dp[m-1][n-1]

        #
        # #新建矩阵版
        # height, width = len(obstacleGrid),len(obstacleGrid[0])
        # store = [[0]*width for i in range(height)]
        #
        # #从上到下，从左到右
        # for m in range(height):#每一行
        #     for n in range(width):#每一列
        #         if not obstacleGrid[m][n]: # 如果这一格没有障碍物 则等于上方和左方格子之和
        #             if m == n == 0: # 或if not(m or n)
        #                 store[m][n] = 1 # 第一行第一个位置，如果无障碍物 则设置为1
        #             else:
        #                 a = store[m-1][n] if m!=0 else 0 # 到达当前格子时 上方格子如果为第0行则直接为0 否则为上方格子路径数
        #                 b = store[m][n-1] if n!=0 else 0 # 到达当前格子时，左方格子如果为0列则直接为0
        #                 store[m][n] = a+b
        # return store[height-1][width-1]

a= Solution()

print(a.uniquePathsWithObstacles(
    [[0,0,0],[0,1,0],[0,0,0]]))
