# encoding: utf-8
# ------------ 腾讯 ---------------
# 监狱数字冲突
# n个房间排在一起，编号1~n,每个房间内都有一个人，现在每个人都要选择1~m的数字，若相邻的房间内选择的数字是一样的，就会发生冲突
# 问发生冲突的情况有多少种（求总情况-所有相邻数字不相等的情况）
# 输入
# 2  3  # ；数字范围 m = 2；房间数量 n = 3
# 输出 对100003取模
# 6     # 6个冲突：（(1,1,1)  (1,1 2)  (1 2 2)  (2 1 1)  (2 2 1)  (2 2 2)  ）

import sys


# # ---------------- dp -------------------
# def main():
#    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
#    m,n = tmp[0],tmp[1]
#    total = m**n
#    dp = [0]*(n+1) # 不发生冲突的情况：所有相邻数字不相等
#    dp[1] = m
#    for i in range(2, n+1):
#       dp[i] = dp[i-1]*(m-1)
#    print(( total - dp[n])%100003) # 发生冲突的情况

# 其实不需要动态规划，可以直接计算

# def main():
#    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
#    m,n = tmp[0],tmp[1]
#    print(m*(m**(n-1)-(m-1)**(n-1))%100003)

# 直接计算容易超时，需要进一步优化--矩阵快速幂
# 构建矩阵递推：一般An与A(n-1)都是按照原始递推式来构建的，
# 当然可以先猜一个An,主要是利用矩阵乘法凑出转移矩阵：T(一定要是常数矩阵)，它能把A(n-1)转移到A(n)
# T：第一行一般就是递推式，后面的行就是不需要的项就让与其的相乘系数为0
# 然后这就是等比数列T * A(n-1)=A(n)，直接写出通项，A1叫初始矩阵；
# 最后用一下矩阵快速幂然后乘上初始矩阵就能得到An,
def main():
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    m, n = tmp[0], tmp[1]
    power = n - 1
    a, b = 1, 1
    basem, basem1 = m, m - 1

    # 快速幂部分，求m和m-1的n-1次方，同时对100003取模了
    while power:
        if power & 1:  # power 奇数 ➡️ 偶数
            a = (a * basem) % 100003
            b = (b * basem1) % 100003
        power >>= 1  # power // 2
        basem = (basem * basem) % 100003
        basem1 = (basem1 * basem1) % 100003

    print (m * (a - b) % 100003)


main()
