'''
在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.

一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.

最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。

给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。

示例：

输入：board = [[1,2,3],[4,0,5]]
输出：1
解释：交换 0 和 5 ，1 步完成
输入：board = [[1,2,3],[5,4,0]]
输出：-1
解释：没有办法完成谜板
输入：board = [[4,1,2],[5,0,3]]
输出：5
解释：
最少完成谜板的最少移动次数是 5 ，
一种移动路径:
尚未移动: [[4,1,2],[5,0,3]]
移动 1 次: [[4,1,2],[0,5,3]]
移动 2 次: [[0,1,2],[4,5,3]]
移动 3 次: [[1,0,2],[4,5,3]]
移动 4 次: [[1,2,0],[4,5,3]]
移动 5 次: [[1,2,3],[4,5,0]]
输入：board = [[3,2,4],[1,5,0]]
输出：14
提示：

board 是一个如上所述的 2 x 3 的数组.
board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-puzzle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def slidingPuzzle(self, board) -> int:
        '''
        这道题解法，注重如何构建一个bfs的问题，如何构建状态，如何构建起始位置作为bfs起点
        只有0的位置才可以移动，这个地方可以理解为 交换两个数字。
        当前位置0 可以和周围上下左右进行交换，交换后的数组状态，可以理解为一个新的状态
        bfs 遍历结束的状态是 符合游戏完成的状态 123 450
        因为数组只有两行三列，此处，可以将二维数组 reshape成一维数组，在判断状态是否满足时简化问题
        :param board:
        :return:
        '''
        # 将二维数组reshape 成一维数组， 记录与之毗邻的节点有哪些，之后交换节点可以作为参考
        # 0 1 2
        # 3 4 5
        neighbor = {0: [1, 3], 1:[0, 2, 4], 2:[1, 5],
                    3:[0, 4], 4:[3, 1, 5], 5:[4, 2]}
        start = ''
        target = '123450'
        # 遍历一遍 数组，获得一维数组的初始状态
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])

        queue = [start]
        # 设定一个遍历过的状态有哪些，避免bfs陷入死循环
        visited = set()
        visited.add(start)
        step = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur == target:
                    return step
                # 找出当前状态中位置为0的位置
                idx = cur.index('0')
                # 该位置的邻接节点位置有哪些，可以交换的位置节点
                for near in neighbor[idx]:
                    new = self.swap(cur, idx, near)
                    # 交换后的新状态是否已经到达过
                    if new not in visited:
                        queue.append(new)
                        visited.add(new)
            step += 1
        return -1

    def swap(self, cur, i, j):
        cur_list = list(cur)
        cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
        return "".join(cur_list)
