# encoding: utf-8
# ------------ 腾讯 ---------------
# 总共有n个怪物，每打一个怪物需要耗费xi的血量，但是会获得yi的金币，一个金币可以购买q点血量
# 用不完的血量所有怪物结束之后不会保留，每一个怪物都可以选择打或者不打
# 问最后结束时，可以获得最大的收益是多少。
# 输入
# 3 2 总共有n个怪物，和一个金币可以购买q点血量
# 1 1 打第一个个怪物的消耗xi和金币收益yi
# 1 10
# 3 1
# 输出
# 10
import math
import sys
import numpy as  np


# ------- 贪心 --------------------
# 贪心算法：如果收益大于消耗就一定去打这个怪物
# 但是收益和消耗需要置换到同一维度，显然以血量为单位比较合适，只需要乘法。打完之后，金币收益累加，消耗血量累加，最后决定买多少血量即可。

def main():
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    n, q = tmp[0], tmp[1]
    loss = np.array([0] * n)
    gain = np.array([0] * n)
    for i in range(n):
        tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
        loss[i], gain[i] = tmp[0], tmp[1]
        if gain[i] * q <= loss[i]:  # 收益小于消耗。# 不打这个怪物
            gain[i] = 0
            loss[i] = 0
    res = int((sum(gain) - math.ceil(sum(loss)) / q))
    print(res)


main()
