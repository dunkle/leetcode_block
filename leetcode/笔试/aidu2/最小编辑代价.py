# 给定字符 s1 和 s2  再给定三个整数 ic dc rc 代表插入,删除、替换 代价
# 输出s1 -> s2 最小操作的代价。
def bianji(s1, s2, ic,dc,rc):
    # 状态转移
    # 两个相等 代价为0
    # 不等
    m = len(s1)
    n = len(s2)
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + ic
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + dc
    for i in range(1,m):
        for j in range(1, n):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + ic, dp[i][j-1] + dc, dp[i-1][j-1]+rc)
    return  dp[m-1][n-1]

s1 = 'abc'
s2 = 'adc'
ic = 5
dc = 3
rc = 2
#
# s1 = 'abc'
# s2 = 'adc'
# ic = 5
# dc = 3
# rc = 100

res = bianji(s1, s2, ic, dc, rc)
print(res)