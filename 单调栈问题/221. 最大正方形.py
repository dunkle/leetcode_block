'''
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def maximalSquare(self, matrix) -> int:
        # 参考最大矩形的做法，最大正方形，也是矩形最大。
        def helper(heights):
            stack = [0]
            lenth = len(heights)
            for i in range(1,lenth):
                while stack and heights[i]<heights[stack[-1]]:
                    # pop之后
                    print(stack)
                    index = stack.pop()
                    height_index = heights[index]
                    # 再取stack最后一个值的index
                    # self.res = max(self.res, (i-stack[-1]-1)*height_index)
                    # 题为正方形，即最短边的平方即为正方形的面积
                    # 此处为 i-stack[-1]-1,而不能为 i-index+1
                    self.res = max(self.res, min((i-stack[-1]-1),height_index)**2)
                stack.append(i)
        self.res = 0
        m = len(matrix)
        n = len(matrix[0])
        heights = [0]*(n+2)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j+1] +=1
                else:
                    heights[j+1] = 0
            helper(heights)
        # heights = [0,2,1,5,6,2,3,0]
        # helper(heights)
        return self.res
a = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
heights = [0,2,1,5,6,2,3,0]
matrix = [["0","1"],["0","1"]]
res = a.maximalSquare(matrix)
print(res)