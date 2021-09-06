class Solution:
    def findCircleNum(self, isConnected) -> int:
        '''
        1、建立节点连接表、建立访问节点初始表
        2、由每一个未被访问的节点作为初始查找节点，找所有连通区域
        时间复杂度 O(n^2) 访问每个节点和连接节点
        空间复杂度 O(n) 记录每个节点是否被访问
        :param isConnected:
        :return:
        '''
        n = len(isConnected)
        from collections import defaultdict
        hashNodecity = defaultdict(list)

        # 初始化每个节点，是否被访问过
        visitNode = [0]*n
        # 建立每个节点相连的节点
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    hashNodecity[i].append(j)
        # print(hashNodecity)
        res = 0
        # 依次遍历每个节点
        for i in range(n):
            # 如果节点没有被访问过，由此找与之相连的节点
            if visitNode[i]==0:
                # 记录每一个初始没被访问过的节点 相当于一个省份
                res+=1
                # 依次遍历与之相连的节点
                queue = [i]
                while queue:
                    node = queue.pop()
                    # 相当于bfs，依次遍历每一层节点，并且把对应的下一层没有访问过的节点放入队列
                    for j in hashNodecity[node]:
                        if visitNode[j]==1:
                            continue
                        visitNode[j] = 1
                        queue.append(j)
        return res

a = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# isConnected = [[1,0,0,1],
#                [0,1,1,0],
#                [0,1,1,1],
#                [1,0,1,1]]
res = a.findCircleNum(isConnected)
print(res)