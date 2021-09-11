'''
节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。

示例1:

 输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
 输出：true
示例2:

 输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]],
  start = 0, target = 4
 输出 true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/route-between-nodes-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findWhetherExistsPath(self, n: int, graph, start: int, target: int):
        from collections import defaultdict
        if start==target:
            return True
        hashNode = defaultdict(set)
        # 建立一个字典，这个字典代表，与第i个节点相连的节点有哪些 graph中的元素[node1, node2]
        for key, value in graph:
            hashNode[key].add(value)
        # print(hashNode)
        visit = [False]*n
        # 队列保存起始节点
        queue = [start]
        while queue:
            # 弹出队列的节点,并且标记当前节点已经访问
            node = queue.pop(0)
            visit[node]= True
            # 如果存在和当前节点 相连的节点，则由此访问其他节点
            if len(hashNode[node])>0:
                # 如果目标节点 与当前节点相连，返回True
                if target in hashNode[node]:
                    return True
                # 否则依次遍历所有与之相连的节点
                for i in hashNode[node]:
                    # 并且节点是没有被访问过的
                    if not visit[i]:
                        queue.append(i)
        return False


a = Solution()
n = 5
graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]]
start = 0
target = 4
res = a.findWhetherExistsPath(n, graph, start, target)