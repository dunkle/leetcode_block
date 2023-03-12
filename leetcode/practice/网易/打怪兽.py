# encoding: utf-8
# ------------ 网易 ---------------
# 共有n个怪兽，每个怪兽欧有两个属性，破防能力和伤害力
# 当勇者的防御力大于怪兽破防能力，勇者不受伤害，否则勇者受到怪兽受害力
# 勇者初时防御力D，每挑战成功一只怪兽防御力可以+1，求打败所有怪兽最少承受多少伤害
# 输入
# 3 50            n = 3；D = 50
# 100 50 51       怪兽的破防能力
# 1000 1000 1000  怪兽的伤害
# 输出
# 1000
# 先挑战第一只怪兽，勇者防御力50<怪兽破防能力100，勇者受到1000伤害，勇者防御力+1
# 之后挑战第二只怪兽，勇者防御力51>怪兽破防能力50，勇者不受伤害，勇者防御力+1
# 最后挑战第三只怪兽，勇者防御力52>怪兽破防能力51，勇者不受伤害，勇者防御力+1
# 一共受到1000伤害

import operator
import sys


# ---------- 双指针 ----------------------
# 如果有能不吃伤害打的，直接打
# 如果没有能不吃伤害打的，直接打破防最强的
def main():
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    n, D = tmp[0], tmp[1]
    defend = list(map(int, sys.stdin.readline().strip().split(' ')))
    attack = list(map(int, sys.stdin.readline().strip().split(' ')))
    monster = []
    for i in range(n):
        monster.append((defend[i], attack[i]))
    monster.sort(key=operator.itemgetter(0))
    res = 0  # 受到的总伤害
    left = 0  # 从前向后打：怪兽攻防能力越来越强，如果D< defend[j]，则后面的都打不过
    right = n - 1  # 从后向前打：怪兽攻防能力越来越若
    while left <= right:  # 判断怪兽是否被打完
        # 从前向后
        while left <= right and D > monster[left][0]:  # 可以打这个怪兽
            D += 1  # 防御力 + 1
            left += 1  # 判断下一个
        # 从后向前
        if left <= right:
            res += monster[right][1]
            D += 1  # 防御力 + 1
            right -= 1  # 判断下一个
    print(res)


main()
