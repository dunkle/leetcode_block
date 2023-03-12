![image-20200904165712666](../../../.assert/image-20200904165712666.png)

给定有向无环图，求从一个点到所有点的最小距离。

Dijtsra最短路问题。

python模板：

~~~python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        K -= 1
        # 构造一个图
        graph = [[float('inf')]*N for _ in range(N)]
        visited = [0] * N
        for u, v, w in times:
            graph[u-1][v-1] = w
            
        # 初始化距离矩阵，原点的距离为0
        dist = [float('inf')]*N
        dist[K] = 0
        # 每次选出一个距离最近的点，利用该点更新到所有点的最短路径
        for i in range(N):
            minn, minv = -1, float('inf')
            
            # 选出一个当前情况下路径最短的点
            for j in range(N):
                if visited[j] == 0 and dist[j] < minv:
                    minn, minv = j, dist[j]
            # 如果没有这种点，说明有的点不可达，直接跳出循环
            if minn == -1:
                break
            # 利用当前的点更新到其他点距离的最短路径
            visited[minn] = 1
            for j in range(N):
                if visited[j] == 0:
                    dist[j] = min(dist[j], dist[minn]+graph[minn][j])
        # 如果存在不可达的点返回-1 
        if float('inf') in dist:
            return -1
        # 返回最长的路径
        return max(dist)
~~~

