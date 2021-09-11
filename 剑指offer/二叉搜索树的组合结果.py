#2、二叉搜索树的组合结果：给定n个不同的自然数，试问能组合出多少棵二叉搜索树。输入n，返回m。
def zuhe(n):
    dp = [0] *(n+1)
    dp[0] = 1
    dp[1] = 1
    # dp[n] = dp[0]*dp[n-1] + dp[1]*dp[n-2]+...dp[n-1]*dp[0]
    # 最外层所有数字遍历
    for i in range(2,n+1):
        # 以每一个为节点分左右子树
        for j in range(1,i+1):
            # dp[j-1] 1-(j-1)可以组合多少左子树 右子树组合i-j
            dp[i] += dp[j-1]*dp[i-j]
    return dp[n]