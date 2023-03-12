# coding=utf-8
# ------------ 腾讯 ---------------
# input
# 2      2组测试
# 4      第一组：4对关系
# 1 2    编号1和编号2在一个圈子
# 3 4
# 5 6
# 1 6
# 4      第二组：4对关系
# 1 2
# 3 4
# 5 6
# 7 8
# output
# 4     第一组：最大的朋友圈有4人
# 2     第二组：最大的朋友圈有2人

import sys


class UnionFind:  # 并查集
    def __init__(self, n):
        self.n = n  # 总人数，用于计算largestNum
        self.parent = list(range(n))  # 索引为i的节点，它的直接父节点为parent[i]
        self.weight = [1] * n  # 并查树的深度， 优化合并
        self.maxDeep = 1  # 并查树的最大深度，用于寻找maxParent
        self.maxParent = 1  # 最大朋友圈的leader

    # 由于parent[i] 仅表示自己的直接父节点，查询两个节点是否相交需要比较它们的根节点是否相同。因此要封装一个查询自己根节点的方法。
    # def get_root(self, i):
    #     while i != self.parent[i]:
    #         i = self.parent[i]
    #     return i

    # 当前每次执行get_root时，需要一层一层的找到自己的父节点，很费时。
    # 由于根节点没有父节点，并且文章开始处提到过如果一个节点没有父节点，那么它的父节点就是自己，因此可以说只有根节点的父节点是自己本身。
    # 现在我们加上一个判断，判断当前节点的父节点是否为根节点，如果不为根节点，就递归地将自己的父节点设置为根节点，最后返回自己的根节点。
    def get_root(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.get_root(self.parent[i])
        return self.parent[i]

    # 通过来比较根节点是否相同来判断两节点是否连通。
    def is_connected(self, i, j):
        return self.get_root(i) == self.get_root(j)

    # 连通两个节点时，我们要将其中一个节点的根节点的parent，设置为另一个节点的根节点。
    # 注意，连通两个节点并非仅仅让两节点自身相连，实际上是让它们所属的集合实现合并。
    # def union(self, i, j):
    #     i_root = self.get_root(i)
    #     j_root = self.get_root(j)
    #     self.parent[i_root] = j_root

    # 由于调用get_root时需要通过不断找自己的直接父节点，来寻找根节点，如果这棵树的层级过深，会导致性能受到严重影响。
    # 因此我们需要在union时，尽可能的减小合并后的树的高度。
    # 在构造函数中新建一个数组weight，weight[i] 表示节点i所在的集合的树的高度。
    def union(self, i, j):
        i_root = self.get_root(i)
        j_root = self.get_root(j)

        if self.weight[i_root] == self.weight[j_root]:
            self.parent[i_root] = j_root
            self.weight[j_root] += 1
            if self.weight[j_root] > self.maxDeep:
                self.maxDeep = self.weight[j_root]
                self.maxParent = j_root
        elif self.weight[i_root] > self.weight[j_root]:
            self.parent[j_root] = i_root
            if self.weight[i_root] > self.maxDeep:
                self.maxDeep = self.weight[i_root]
                self.maxParent = i_root
        else:
            self.parent[i_root] = j_root
            if self.weight[j_root] > self.maxDeep:
                self.maxDeep = self.weight[j_root]
                self.maxParent = j_root

    def largestNum(self):
        res = 0
        for i in range(self.n):  # i 的leader是最大朋友圈的leader，则i在这个最大的朋友圈中，朋友圈人数+1
            if self.get_root(i) == self.maxParent:
                res += 1
        return res


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = [2] * n  # 结果
    for i in range(n):  # n test
        m = int(sys.stdin.readline().strip())
        relation = [0, 0] * m  # 总关系数
        totalPerson = 0  # 总人数
        for j in range(m):
            relation[j] = list(map(int, sys.stdin.readline().strip().split(' ')))
            if relation[j][0] > relation[j][1] and relation[j][0] > totalPerson:
                totalPerson = relation[j][0]
            if relation[j][1] > relation[j][0] and relation[j][1] > totalPerson:
                totalPerson = relation[j][1]
        s = UnionFind(1 + totalPerson)  # 初始化：第一位0，因为人的index从1开始
        for j in range(m):
            for k in range(m):
                if j == k:
                    s.union(relation[j][0], relation[k][1])  # 直接朋友
                else:
                    if s.is_connected(relation[j][0], relation[k][0]):  # 间接朋友
                        s.union(relation[j][0], relation[k][0])
        ans[i] = s.largestNum()  # 最大朋友圈的人数
    for i in range(n):
        print(ans[i])
