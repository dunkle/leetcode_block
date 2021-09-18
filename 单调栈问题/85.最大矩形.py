'''
85. 最大矩形
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = []
输出：0
示例 3：

输入：matrix = [["0"]]
输出：0
示例 4：

输入：matrix = [["1"]]
输出：1
示例 5：

输入：matrix = [["0","0"]]
输出：0
提示：

rows == matrix.length
cols == matrix[0].length
0 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'
'''
class Solution:
    def maximalRectangle(self, matrix) -> int:
        # time O(mn), space O(n)
        if not matrix or not matrix[0]:
            return 0

        self.res = 0
        # 此处为柱状图中最大矩形对应的代码
        def helper(arr):
            stack = []
            for i in range(len(arr)):
                while stack and arr[i] < arr[stack[-1]]:
                    idx = stack.pop()
                    width = i - stack[-1] - 1
                    height = arr[idx]
                    self.res = max(self.res, width * height)

                stack.append(i)


        r, c = len(matrix), len(matrix[0])
        # 首尾多加0，方便设置哨兵节点，包含首尾元素的面积求和
        cnts = [0] * (c + 2)
        # 求矩形里最大的矩形，则先统计每一列的最大高度，作为height值
        for i in range(r):
            for j in range(c):
                # 此处统计以i行为底的每一列的高度trick
                if matrix[i][j] == '1':
                    # 以cnt始终记录的是当前列所在的高度，如果当前matrix为1直接基于上次的cnt结果+1
                    # 否则为0
                    cnts[j + 1] += 1
                else:
                    cnts[j + 1] = 0
            # 计算以当前行i为底的最大矩形有多大
            helper(cnts)

        return self.res
