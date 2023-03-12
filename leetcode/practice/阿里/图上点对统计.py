import sys


# ------------ 阿里 ---------------
# n个点m条边的无向带权联通图，
# 两个点之间的路径可能有很多条，只需要找花费最小的路径
# 花费为路径中的最大边权值
# 求满足路径为k的节点对数量
# 输入
# 5 4 3
# 1 2 1
# 1 3 2
# 1 4 3
# 1 5 4
# 输出
# 3

# 返回 start 连接的所有点，放入pass_nodes：set
def BFS(start, edge, pass_nodes):
    if start in pass_nodes:
        return set()
    else:
        pass_nodes.add(start)
        if start in edge:
            for node in edge[start]:
                pass_nodes.update(BFS(node, edge, pass_nodes))
        return pass_nodes


def main():
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    n, m, k = tmp[0], tmp[1], tmp[2]
    edge = {}    # 记录边权重小于k的边
    center = []  # 记录边权重等于k的边
    for i in range(m):
        tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
        if tmp[2] == k:
            center.append([tmp[0], tmp[1]])
        if tmp[2] < k:
            if tmp[0] in edge:
                old = edge[tmp[0]]
                new = old + [tmp[1]]
                edge[tmp[0]] = new
            else:
                edge[tmp[0]] = [tmp[1]]
            if tmp[1] in edge:
                old = edge[tmp[1]]
                new = old + [tmp[0]]
                edge[tmp[1]] = new
            else:
                edge[tmp[1]] = [tmp[0]]

    res = 0
    while center:
        tmp = center.pop()
        start, end = tmp[0], tmp[1]
        near_start_num = set()
        near_start_num = BFS(start, edge, near_start_num)
        near_end_num = set()
        near_end_num = BFS(end, edge, near_end_num)

        # near_start_num 和 near_end_num 无交集，说明start 和 end 不连通
        if not near_start_num.intersection(near_end_num):
            res += len(near_start_num) * len(near_end_num)

    print(res)


main()
