# encoding: utf-8
# ------------ 美团 ---------------
# n个点，m条边组成的无向图，每条边有一定长度
# 从出发点开始跑步，每次都选择最短路径前往其他目的地，求目的地距离起点k米后的个数（点或边上均可），若不存在则输出0
# 输入
# 3 3 1  点数n = 3；边数m = 3；起点编号s = 1
# 1 2 2  点1和点2之间有一条无向边，长度2
# 2 3 3  点2和点3之间有一条无向边，长度3
# 1 3 4  点1和点3之间有一条无向边，长度4
# 4      跑步 k = 4
# 输出
# 2

import sys
import numpy as np
import math


# -----------  Floyd + DFS + set -------------------


def DFS(Distance, path, passby, k): # passby:记录路径
    num = 0
    for i in range(1, len(path)):
        if i not in passby and path[passby[-1]][i] == passby[-1]:  # 已有路径的最后一个点 → i 的最短路径是直连
            if Distance[passby[0]][i] >= k:
                num += 1
                passby = [passby[0]]  # 重置以记录下一个路径
            else:
                passby.append(i)
                num += DFS(Distance, path, passby, k)
    return num


def main():
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    n, m, s = tmp[0], tmp[1], tmp[2]

    # 创建边权重矩阵 (n+1)*(n+1)
    # inf：表示两点之间不相连
    weight = [[float("inf") for i in range(n + 1)] for i in range(n + 1)]
    # 0：表示自身
    for i in range(1, n + 1):
        weight[i][i] = 0
    # 0：初始化其他权重
    for i in range(m):
        edge = list(map(int, sys.stdin.readline().strip().split(' ')))
        weight[edge[0]][edge[1]] = edge[2]
        weight[edge[1]][edge[0]] = edge[2]

    # -----------  Floyd：多源最短路径 -----------------
    # 创建路径矩阵 (n+1)*(n+1)；记录点点之间最短路径的第二条路径的起点
    path = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        for j in range(n + 1):
            if not math.isinf(weight[i][j]) and weight[i][j]:
                path[i][j] = i

    # 创建距离矩阵(n+1)*(n+1)，记录最短路径的权重之和
    Distance = weight[:]

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if Distance[i][k] + Distance[k][j] < Distance[i][j]:
                    Distance[i][j] = Distance[i][k] + Distance[k][j]
                    path[i][j] = path[k][j]
    # print('result:Distance', Distance)
    # print('result:path', path)

    # Start running
    k = int(input())
    passby = [s]
    res = DFS(Distance, path, passby, k)
    print(res)


main()
