class Solution:
    def getMaxMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = matrix[0][0]
        # 给第一列 赋值为数组第一列元素
        for j in range(m):
            dp[j][0] = matrix[j][0]
        print("初始化第一列", dp)
        # 每一行求累积和
        for i in range(m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1]+ matrix[i][j]
        print("行累积和",dp)
        # 求到(i,j)位置 构成矩形的累积和
        for j in range(1,n):
            for i in range(1,m):
                dp[i][j] = dp[i-1][j]+dp[i][j]
        print(dp)
        # 计算任意两个点组成的矩形区域累积和
        area = matrix[0][0]
        res = []

        for i in range(m):
            for j in range(n):
                start = (i,j)
                for k in range(i,m):
                    for t in range(j,n):
                        end = (k,t)
                        tmp_area = dp[end[0]][end[1]] - dp[end[0]][start[1]]-dp[start[0]][end[1]]+dp[start[0]][start[1]]
                        bianyuan = 0
                        for col in range(start[1], end[1]):
                            bianyuan +=matrix[start[0]][col]
                        for row in range(start[0], end[0]):
                            bianyuan += matrix[row][start[1]]
                        tmp_area +=bianyuan
                        tmp_area -= matrix[start[0]][start[1]]
                        if tmp_area>area:
                            area = tmp_area
                            res = [start[0], start[1], end[0], end[1]]
        print('res', res)
        return res


a = Solution()
matrix = [
    [-1,0,1],
    [0,-1,1],
    [0,-1,1],
]

matrix = [[9,-8,1,3,-2],
          [-3,7,6,-2,4],
          [6,-4,-4,8,-7]]


# print(matrix)
a.getMaxMatrix(matrix)