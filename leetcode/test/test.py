# 编辑距离
# 两个字符串 的编辑距离
# abcdef
# abceef
# 增加 删除 替换 距离+1
def distanc(s1, s2):
    '''
    s1[i] ==s2[j]
    dp[i][j] = dp[i-1][j-1]
    # 不等
    dp[i][j] = min(dp[i-1][j], dp[i][j-1])
    :param s1:
    :param s2:
    :return:
    '''
    m = len(s1)
    n = len(s2)
    dp = [[0 for i in range(n)] for j in range(m)]
    if s1[0]==s2[0]:
        dp[0][0] = 0
    else:
        dp[0][0] = 1

    # 初始化dp
    for i in range(1, m):
        # s2 只有一个字符，s1有i个字符
        if s1[i]==s2[0]:
            dp[i][0] = i-1
        else:
            dp[i][0] = dp[i-1][0]+1

    for i in range(1,n):
        # s1 只有一个字符， s2 有i个字符
        if s1[0] == s2[i]:
            # 如果s2长度的字符 与s1有一个相同，那么需要删除其他i-1
            dp[0][i] = i-1
        else:
            # 如果
            dp[0][i] = dp[0][i-1]+1

    for i in range(1, m):
        for j in range(1, n):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
    return dp[m-1][n-1]
s1=  'abcdef'
s2 = 'abceef'
res = distanc(s1,s2)
print(res)