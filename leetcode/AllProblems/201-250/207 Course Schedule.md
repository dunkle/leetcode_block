# 207. Course Schedule

![image-20200426152654400](../../../.assert/image-20200426152654400.png)

给定一些课程及其预备课程，判断是否有相互依赖。

## 拓扑排序

### DFS

对每个节点进行dfs，设置vis数组标识是否访问过，其中：
$$
\text{vis}[i] = \begin{cases}
1, \quad 访问过 \\
0, \quad 未放问 \\
-1, \quad 正在访问中
\end{cases}
$$
如果在dfs的过程中发现某个vis为-1则说明有环。

~~~python
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.G = defaultdict(list)
        for p in prerequisites:
            self.G[p[0]].append(p[1])
        
        self.vis = [0]*(numCourses+1)
        for i in range(1, numCourses+1):
            if not self.dfs(i):
                return False
            
        return True
        
    def dfs(self, c):
        
        self.vis[c] = -1
        for pre in self.G[c]:
            if self.vis[pre] < 0:
                return False
            elif self.vis[pre] > 0 :
                continue
            elif not self.dfs(pre):
                return False
               
        self.vis[c] = 1
        return True
~~~

时间复杂度$O(N+E)$N为节点的数量，E为边的数量。

### BFS

先找入度为0的节点，如果没有找到则有环。从入度为0的节点开始，将该节点的入度置为-1表示已访问过，将以该节点为预备课程的节点的入度-1，重复该过程。