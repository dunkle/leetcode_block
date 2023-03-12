'''
节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。

示例1:

 输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
 输出：true
示例2:

 输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
 输出 true
提示：

节点数量n在[0, 1e5]范围内。
节点编号大于等于 0 小于 n。
图中可能存在自环和平行边。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/route-between-nodes-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findWhetherExistsPath(self, n: int, graph, start: int, target: int) -> bool:
        #初始化连接表
        link_table = [[] for i in range(n)]
        #与第 i 个节点相连的节点 有哪些 记录下来
        for i in graph:
            link_table[i[0]].append(i[1])
        # 记录第i个节点有没有被访问
        visitnode = [0 for i in range(n)]
        que = []
        que.append(start)
        while que:
            node = que.pop()
            # 判断目标节点是否在当前访问节点的连接节点里
            if target in link_table[node]:
                return True
            # 将当前节点的连接节点放入 que中，只有未被访问过的节点才放入其中
            for node_k in link_table:
                if visitnode[node_k]==0:
                    que.append(link_table[start])
            # 标记当前节点为 被访问过的节点
            visitnode[node] = 1
        return False