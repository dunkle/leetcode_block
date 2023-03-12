# encoding: utf-8
# ------------ 腾讯 ---------------
# 有n个物品，每个物品k个属性
# 求完美对个数：第i个物品的第1个属性+第j个物品的第1个属性 = 第i个物品的第2个属性+第j个物品的第2个属性 = 。。=  第i个物品的第k个属性+第j个物品的第k个属性
# 输入
# 5 3        # n = 5；k = 3
# 2 11 21    # 第1个物品的3个属性值
# 19 10 1
# 20 11 1
# 6 15 24
# 18 27 36   # 第5个物品的3个属性值
# 输出
# 3          # 有3个完美对 1-3 2-4 2-5
import sys

# def main():
#     tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
#     n,item_k = tmp[0], tmp[1]
#     attribute = [[0 for i in range(item_k)] for i in range(n)]
#     res = 0
#     for i in range(n):
#         attribute[i] = list(map(int, sys.stdin.readline().strip().split(' ')))
#     for i in range(n-1):
#         for j in range(i+1,n):
#             tmp = attribute[i][0] + attribute[j][0]
#             k = 1
#             while k<item_k and (attribute[i][k] + attribute[j][k]) == tmp :
#                 k += 1
#             if k == item_k:
#                 res += 1
#     print(res)

# 复杂度太高，只能过0.3的用例。
# 考虑到每一个数据，只需要对第一个数据做差就能根据第一属性之后的值找到它的完美配对。
# 建立一个哈希表，只存储第二个属性开始减第一个属性的值，
# 如果有一个物品从第二个属性开始，也对那个物品的第一个属性值做差，相当于aij+akj−ai0−ak0=0 则是完美匹配。
# 这样就可以把每一种情况使用哈希表存储，快速求出与之对应的完美匹配是否存在。
# 如果存在，存在的数目是多少，可以与所有的情况构成完美配对，就加上这个数即可。

from collections import defaultdict


def main():
    n, k = [int(i) for i in input().split(' ')]
    dict = defaultdict(lambda: 0)
    # 使用defaultdict,任何未定义的key都会默认返回一个根据method_factory参数不同的默认值;
    # 而相同情况下dict()会返回KeyError.
    b = [0] * (k - 1)    # 辅助空间
    res = 0

    for j in range(n):
        attribute = [int(i) for i in input().split(' ')]
        for i in range(1, k):
            attribute[i] -= attribute[0]  # 每个属性减第一个属性的值
            b[i - 1] = -attribute[i]  # 每个值取相反数
        if tuple(b) in dict:  # 所有相反数组成元组，若在dict存在对应元组，说明该元组与其元组求和为0
            res += dict[tuple(b)]  # 对应元组个数
        dict[tuple(attribute[1:])] += 1  # key：tuple；value：出现次数（输入行数）

    print(res)


main()
