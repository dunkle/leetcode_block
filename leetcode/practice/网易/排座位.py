# coding=utf-8
# ------------ 网易 ---------------
# 题目
#   恰好数量的横排连坐
#   有些同学不愿意坐在一起
#   求所有可能的安排情况
# 输入
# 3 2       n：总人数；k：关系不好的对数
# 1 2       x！=y 但关系对可能重复
# 2 1
# 输出：
# 1 3 2     每行输出一组解
# 2 3 1     按字典从小到大
import sys


def main():
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    n = tmp[0]  # 总人数
    k = tmp[1]  # 关系不好的对数

    # ---------- 字典：关系表 ---------------
    d = dict.fromkeys(list(range(1, n+1)), [])  # 从1开始为人的index
    for i in range(k):
        tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
        # 字典添加对应元素
        old = d[tmp[0]]
        new = old + [tmp[1]]
        d[tmp[0]] = new
        # 关系不好是相互的
        old = d[tmp[1]]
        new = old + [tmp[0]]
        d[tmp[1]] = new

    # ---------- DFS + 回溯法安排座位 ---------------
    seat = []  # 座次表
    stack = list(range(1, n+1))+[0]  # 第一个位置，有n个候选人
    i = 0
    while stack:
        stack.pop()
        if not stack:
            break
        candidate = stack.pop()
        stack.append(0)                  # 为了回溯
        print("candidate", candidate)
        if candidate:
            seat.append(candidate)       # 当前位置
            i += 1  # 下一个位置
            if i == n:                   # 全部排完一次
                print(seat)              # 打印座次表
                stack.append(0)          # 为了回溯
            else:
                for j in range(1, n+1):  # 关系好而且没有被排过的
                    if (j not in seat) and (j not in d[candidate]):
                        stack.append(j)  # 入栈
                stack.append(0)          # 为了回溯
        else:
            seat.pop()                    # 回溯
            i -= 1                        # 下一个位置
        print("stack", stack)
        print("seat", seat)







main()
