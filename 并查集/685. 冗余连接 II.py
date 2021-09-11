from collections import defaultdict
class unionfind:
    # 初始化中每一个节点的父节点就是它自己
    def __init__(self,n):
        self.father=defaultdict(int)
        for i in range(1,n+1):
            self.father[i]=i
    # 将u->v加入并查集 u的祖先的father 变成v的祖先
    #「注意」不是u的father变成v 而是u和v的祖先
    def union(self, u, v):
        root_u, root_v=self.find(u), self.find(v)
        if root_v!=root_u:
            self.father[root_v]=root_u
        return
    # 找到u的祖先节点
    def find(self, u):
        root=self.father[u]
        while self.father[root]!=root: root=self.father[root]
        return root

#下面的代码只能通过部分测试用例 比如edges=[[2,1],[3,1],[4,2],[1,4]]就会fail
def findRedundantDirectedConnection(edges):
    n=1 # n一开始未知
    # edges=[u->v] 先计算各节点的入度
    in_degree=defaultdict(int)
    out_degree=defaultdict(int)
    edges_2=[] # 用以保存u->v且v的入度为2的边
    # 获取每个点的入度
    for u,v in edges:
        n=max(n,u,v)
        in_degree[v]+=1
        out_degree[u]+=1
    for u, v in edges:
        if in_degree[v]==2:
            edges_2.append([u,v])
    # 根据edges建立并查集 并在建立过程中找的导致图成环的最后一个边 (如果有环)
    # 因为如果两个点所在的边在添加图之前就是相同的根，那么这条边添加上之后 这个图一定不是树了
    uf=unionfind(n)
    edge_loop=[]
    for u,v in edges:
        # 添加 u->v 时 如果u的祖先是v说明存在有向路径 v->...->u 所以有环
        if uf.find(u)==v:
            edge_loop.append([u, v])
        uf.union(u,v)
        # print('add {}->{}, u={} v={} root[{}]={}'.format(u,v,u,v,v,uf.find(v)))
    # 情况1: 如没有入度为2的边 说明存在有向环 删除最后一个使得构成非环的节点
    if len(edges_2)==0:
        return edge_loop[0]
    # 情况2: 如果有两个end入度为2的边(只能是两个) 则删除其中一个 使得剩下的图没有环
    u, v=edges_2[1] # u->v
    if edge_loop:   # 如果有环 则删除环内的边
        if uf.find(u)==v:
            return edges_2[1]
        else:
            return edges_2[0]
    else:
        return edges_2[1] # 否则 删除后一个