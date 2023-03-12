# coding=utf-8
# 请使用标准输出(sys.stdout)；勿使用图形、文件、网络、系统相关的操作，如Process , httplib , os
# 缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用
# 如果使用sys.stdin.readline，因为默认会带换行符，所以要strip(' ')进行截取；建议使用input()

# ------------ 美团 ---------------
# 超市物品n件，分为两类
#     含有A类，买的所有物品中最便宜的一件半价
#     只有B类，不打折
# 一共k个人购买商品，每个人只能付款一次，价格不限，求如何购买价格最低（保留两位小数）
# 输入：
# 5 2   物品 n = 5; 人 k = 2
# 10 1  物品1价格p = 10；属于A类
# 2 2   物品2价格p = 2；属于B类
# 5 2
# 8 1
# 9 1
# 输出：
# 28.00 第一个人只买物品1；第二个人买剩下的物品（买法不唯一）

# 思路：该问题本质上是海量输入数据中找出前k个最大值
# -------------- 最大堆：前k个最大值 ------------------

import heapq
import sys


def MaxHeap(arr, k):  # 最大堆
    max_heap = []
    length = len(arr)
    if not arr or k <= 0 or k > length:
        return
    k = k - 1
    for ele in arr:
        if len(max_heap) <= k:
            heapq.heappush(max_heap, ele)
        else:
            heapq.heappushpop(max_heap, ele)
            # heappushpop(a, x) 将x插入到堆中后，弹出堆中的最小值。
            # heapreplace() 弹出堆中的最小值后，将x插入到堆中。

    return map(lambda x: x, max_heap)


def MinHeap(arr, k):  # 取反+最大堆 = 最小堆
    max_heap = []
    length = len(arr)
    if not arr or k <= 0 or k > length:
        return
    k = k - 1
    for ele in arr:
        ele = -ele
        if len(max_heap) <= k:
            heapq.heappush(max_heap, ele)
        else:
            heapq.heappushpop(max_heap, ele)

    return map(lambda x: -x, max_heap)


def main():
    arr = [10, 9, 8]
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    n, k = tmp[0], tmp[1]
    minA, minB = float('inf'), float('inf')
    sumA, sumB = 0, 0
    A = []
    for i in range(n):
        tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
        item_price, item_type = tmp[0], tmp[1]
        if item_type == 2:  # B类不打折，所以全部一组
            sumB += item_price
            if minB > item_price:
                minB = item_price
        else:
            sumA += item_price
            A.append(item_price)
            if minA > item_price:
                minA = item_price

    if len(A) < k:  # A类不足k个
        total = sumB + sumA / 2
    elif len(A) == k:  # A类k个,第k个人购买：B全部+最小的A；discount：A/B的最小值的一半
        if minA < minB:
            total = sumB + sumA / 2
        else:
            total = sumB - minB / 2 + sumA / 2 + minA / 2
    else:  # A类多余k个
        # 第k个人购买：B全部+剩余的A；discount：A/B的最小值的一半
        discount = minA if minA < minB else minB
        # 前k-1个人购买：前k-1个最大的A；discount：前k-1个最大的A的一半
        maxA = MaxHeap(A, k - 1)
        discount += sum(maxA)
        total = sumB + sumA - discount / 2

    print("%.2f" % total)  # （保留两位小数）


if __name__ == '__main__':
    main()
