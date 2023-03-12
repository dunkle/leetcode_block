# 210. Course Schedule II

![image-20200509185519124](../../../.assert/image-20200509185519124.png)

同样是拓扑排序，这次需要输出访问课程的顺序。

从入度为0的课程开始访问，然后将依赖这些课程的课程入度减1，不断重复这个过程。

用字典包含需要某门课程的课程。

~~~python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegress = [0 for i in range(numCourses)]
        
        adj_list = defaultdict(list)
        zero_indegrees_list = []
        indegrees = [0 for _ in range(numCourses)]
        for p, q in prerequisites:
            adj_list[q].append(p)
            indegrees[p] += 1
        
        for i, n in enumerate(indegrees):
            if n == 0:
                zero_indegrees_list.append(i)
            
        result = []
        while zero_indegrees_list:
            
            v = zero_indegrees_list.pop(0)
            result.append(v)
            if v in adj_list:
                for n in adj_list[v]:
                    indegrees[n]-=1
                    if indegrees[n] == 0:
                        zero_indegrees_list.append(n)
                del adj_list[v]
        
        return result if len(result) == numCourses else []
~~~

