# encoding: utf-8
# ------------ 腾讯 ---------------
# 抛物线：y2 = 2Ax；直线：y = Bx + C
# 求围出的面积，若不存在输出0
# 输入
# 1      # T组测试数据
# 1 1 -6 # A = 1；B = 2；C = -6
# 输出
# 31.2481110540 # 每组测试的答案

# 定积分处理：
# 1 先求交点：第一个函数是 y 的二次函数，看起来不方便，把x和y交换，然后联立方程求交点，就能得到二次函数，最后化简得到判别式 > 0 则两个交点存在面积，否则不存在面积。
# 2 求积分：
#       数值分析：把一个函数切分成很多矩形或者梯形，然后把矩形(梯形)的面积累加----超时；
#       应该是要对这个二次函数手动求定积分，找到被积函数的原函数，然后带入上下限进行计算。

import sys
import math


def main():
    n = int(sys.stdin.readline().strip())
    num = list(map(int, sys.stdin.readline().strip().split(' ')))
    sum = [0] * n  # 初始化：不存在面积
    for i in range(n):
        a, b, c = num[0], num[1], num[2]
        deta = 4 * a * (a - 2 * b * c);
        if deta > 0:  # deta>0：方程有两个解，两解之间存在面积；deta=0：方程有一个解，deta<0：方程无解，都不存在面积
            deta1 = math.sqrt(deta)
            x1 = a / b + 0.5 * deta1 / b;  # / 浮点数除法
            x2 = a / b - 0.5 * deta1 / b;
            sum[i] = (x2 ** 3 / (6 * a) - x2 ** 2 / (2 * b) + x2 * c / b) - (
                        x1 ** 3 / (6 * a) - x1 ** 2 / (2 * b) + x1 * c / b)
            print(sum[i])
    for i in range(n):
        print(sum[i])


main()
