# encoding: utf-8
# ------------ 阿里 ---------------
# 从m种乒乓球中购买n个乒乓球，第一种至少会买一个
# 若两种购买方案的某种乒乓球数量不同，则认为这两种购买方案不同
# 求共有多少种方案（对10^9+7取模）
# 输入
# 2 2   n = 2；m = 2
# 输出
# 2     方案2：（1，1）；（1，2）
import sys


def factorial(n):  # 动态规划求阶乘
    dp = [i for i in range(n + 1)]
    dp[0] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i] * dp[i - 1]
    return dp


def main():
    n, m = [int(i) for i in input().split(' ')]

    # --------- 组合 + 动态规划求阶乘 -----------------
    # total = 0
    # if m < n - 1:  # 种类数小于位子数
    #     dp = factorial(n - 1)
    #     for i in range(1, m + 1):
    #         # 组合：从m类中选出1～m类  C_m_i= m!/i!*(m-i)!
    #         combination = dp[m] / dp[i] * dp[m - i]
    #         # 排列：将 n-1 个位置分给i类，划 i-1 刀 A_(n-2)_(i-1) = (n-2)! / ((n-2-(i-1))!
    #         partition = dp[n-2] / dp[n-i-1]
    #         total += combination * partition
    # else:
    #     dp = factorial(m)
    #     for i in range(1, n):
    #         combination = dp[m] / dp[i]* dp[m - i]
    #         partition = dp[n - 2] / dp[n - i - 1]
    #         total += combination * partition
    # print(int(total))

    # --------- 动态规划 -----------------
    # 第一种至少会买一个，一共买n个，所以实际计算n-1个位置：0～n-2
    # 位置 0
    exploration = [m] * (n - 1)  # 探索
    exploitation = [0] * (n - 1)  # 利用
    # 位置 1～n-2
    for i in range(1, n - 1):
        # --- 利用：新加入的类型是之前的方案中已有的类型 ------------------
        for j in range(0, i):
            # 之前的每一轮探索*类型
            exploitation[i] += exploration[j] * (j + 1)

        # ---- 探索：新加入的类型是之前的方案中没有的类型 ------------------
        if i <= m:
            exploration[i] = exploration[i - 1] * (m - i) / (i + 1)
        else:  # 种类数小于位数,停止探索
            exploration[i] = 0

    print(int(exploitation[n - 2] + exploration[n - 2]))


main()
