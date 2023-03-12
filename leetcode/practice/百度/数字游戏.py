# coding=utf-8
# ------------ 百度 ---------------
# 题目
#   小W在黑板上写出了一行数字a1，a2，a3，……，an，
#   每回合你可以从中选择一个数字擦去它，接着剩下来的每个数字ai都要递减一个值bi,即a1减掉b1,a2减掉b2,….。
#   如此重复M个回合，所有你擦去的数字之和就是你所得的分数。
# 输入
# 3         第一行是一个整数n（1<=n<=2000），表示数字个数；
# 3         第二行一个整数m（1<=m<=n），表示回合数，
# 10 20 30  第三行有n个不超过10000的正整数，a1，a2，a3，……，an表示原始序列，
# 4 5 6     最后一行有n个不超过500的正整数，b1，b2，b3，……，bn，表示每回合每个数字递减的值。
# 输出：
# 47        输出文件只有一个整数，表示最大的可能得分。
import operator
import sys
def main():
    n = int(sys.stdin.readline().strip())  #数字个数
    m = int(sys.stdin.readline().strip())  #回合数
    memo = []*n
    a = list(map(int, sys.stdin.readline().strip().split(' ') ))
    b = list(map(int, sys.stdin.readline().strip().split(' ') ))
    for i in range(n):
        memo.append((a[i], b[i]))
    memo.sort(key= operator.itemgetter(1),reverse = True) # b从大到小排序;a从小到大排序
    dp = [[0]*(m+1)]*(n+1) # 前i个数中取j个数所能获得的最大数字和，为避免f[i-1][j]出现 i-1<j 多给一位
    memo = [(0,0)]+memo  #配合dp，多给一位

    for i in range(1,n+1):
        for j in range(1,m+1):
            if j <= i: #f[i][j] 就会有两个可能的状态转移过来，即为选或不选当前这个点。
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+memo[i][0]-memo[i][1]*(j-1))
    print(dp[n][m]) #最大的可能得分

main()
