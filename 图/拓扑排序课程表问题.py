'''
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，
其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
提示：
1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
prerequisites[i] 中的所有课程对 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        '''
        1、遍历每个节点，用字典存储每个节点与之相连的节点
        2、同时统计每个点的入度
        3、入度为0的点存入队列
        4、队列节点弹出代表对应的课程+1
        https://leetcode-cn.com/problems/course-schedule/solution/bao-mu-shi-ti-jie-shou-ba-shou-da-tong-tuo-bu-pai-/
        :param numCourses:
        :param prerequisites:
        :return:
        '''
        from collections import defaultdict
        hashNode = defaultdict(set)
        # 记录每个节点的入度
        indegree = [0 for i in range(numCourses)]
        #建立邻接表，记录每个节点的后继节点
        for second, first in prerequisites:
            hashNode[first].add(second)
            # 并且统计对应节点的入度
            indegree[second] +=1

        # 把所有入度为0点加入 queue队列中，代表可以直接学习该课程
        queue = []
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)

        # 结果值
        count = 0

        while queue:
            # 每次弹出队列的节点，代表，该课程为先修课程，入度为0不需要学习其他课程
            node = queue.pop(0)
            count+=1
            # 每次学完当前课程之后，所有以该课程为先修课程的后继节点 入度-1
            for successor in hashNode[node]:
                indegree[successor]-=1
                # 如果入度变为0，那么下次可以直接学习该课程，因此需要入队
                if indegree[successor]==0:
                    queue.append(successor)
        # count 代表一共可以学习多少门课程，如果和所有课程数相等，代表可以学完
        return count==numCourses
