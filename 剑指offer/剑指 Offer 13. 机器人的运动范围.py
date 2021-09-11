'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？
示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 初始标记所有位置为False
        dp = [[False for i in range(n)] for j in range(m)]
        # 起始点位置标记为 True
        dp[0][0] = True
        # 代表可达结果 +1
        res = 1
        # 初始化 沿着第一行可达位置
        for x1 in range(1, n):
            x11 = x1%10
            x12 = x1//10
            # 只有当前坐标数位小于k并且上一个位置可达，代表当前位置可达
            if x11+x12<=k and dp[0][x1-1]:
                res+=1
                dp[0][x1] =True
        # 初始化沿着第一列
        for x1 in range(1, m):
            x11 = x1%10
            x12 = x1//10
            if x11+x12<=k and dp[x1-1][0]:
                res+=1
                dp[x1][0]= True

        # 判断数位和是否小于k
        def is_k(x1,y1):
            x11 = x1%10
            x12 = x1//10
            y11 = y1%10
            y12 = y1//10
            if x11+x12+y11+y12<=k:
                return True
            return False
        # 判断是否可以从四周上下左右，到达当前位置
        def is_round(x1, y1):
            steps = [(-1,0), (0,-1), (1,0),(0,1)]
            for step in steps:
                newx1 = step[0]+x1
                newy1 = step[1]+y1
                if 0<=newx1<m and 0<=newy1<n and dp[newx1][newy1]:
                    return True
            return False
        # 遍历所有位置
        for x1 in range(1, m):
            for y1 in range(1, n):
                # 当前数位满足小于等于k并且可以从周围位置到达当前位置
                if is_k(x1,y1) and is_round(x1, y1):
                    dp[x1][y1] = True
                    res+=1
        return res

a = Solution()
m=38
n=15
k=9
fi = 135
# 16
# 8
# 4

# dp = [(x, y) for x in range(n) for y in range(m)]
# print(dp)
res = a.movingCount(m,n, k)
print(res)