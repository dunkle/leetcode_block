class Solution:
    def gardenNoAdj(self, N: int, paths):
        if not paths: return [1] * N  # 无边图，一种颜色就够用了
        g = [[] for i in range(N)]  ##g[i]表示第i个节点相邻的所有的节点序号
        ans = [0 for i in range(N)]  ##ans[i]表示第i个节点所上的颜色
        for x, y in paths:  ##此过程来填充g
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        for i in range(N):  ##为每个节点上色
            ##以下语句：任意节点在其相邻节点没有使用过的颜色中随机选取一个上色
            ans[i] = ({1, 2, 3, 4} - {ans[j] for j in g[i]}).pop()
        print(ans)
        return ans


'''
N = 3, paths = [[1,2],[2,3],[3,1]]
'''

N = 3
paths = [[1, 2], [2, 3], [3, 1]]

N = 4
paths = [[1, 2], [3, 4]]
a = Solution()
a.gardenNoAdj(N, paths)
