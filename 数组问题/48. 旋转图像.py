'''
        给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

        你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/rotate-image
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def rotate(self, matrix) -> None:
        """
        考虑围绕中心点的 四个点
        """
        m = len(matrix)
        print(m)
        for i in range(m//2):
            # print(i)
            for j in range(i, m-2*i):
                # print(i, j)
                # print(matrix[i][j], matrix[j][m-i-1], matrix[m-i-1][m-j-1], matrix[m-j-1][i])
                matrix[i][j], matrix[j][m-i-1], matrix[m-i-1][m-j-1], matrix[m-j-1][i] = matrix[m-j-1][i], matrix[i][j], matrix[j][m-i-1], matrix[m-i-1][m-j-1]
                # print(matrix[i][j], matrix[j][m-i-1], matrix[m-i-1][m-j-1], matrix[m-j-1][i])
                for i in range(len(matrix)):
                    print(matrix[i])
                print("*******")
        return matrix
#
# class Solution:
#     def rotate(self, matrix) -> None:
#         pos1,pos2 = 0,len(matrix)-1
#         while pos1<pos2:
#             add = 0
#             while add < pos2-pos1:
#                 #左上角为0块，右上角为1块，右下角为2块，左下角为3块
#                 temp = matrix[pos2-add][pos1]
#                 matrix[pos2-add][pos1] = matrix[pos2][pos2-add]
#                 #3 = 2
#                 matrix[pos2][pos2-add] = matrix[pos1+add][pos2]
#                 #2 = 1
#                 matrix[pos1+add][pos2] = matrix[pos1][pos1+add]
#                 #1 = 0
#                 matrix[pos1][pos1+add] = temp
#                 #0 = temp
#                 add = add+1
#             pos1 = pos1+1
#             pos2 = pos2-1
a = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# matrix = []
for i in range(len(matrix)):
    print(matrix[i])
# print(matrix)
a.rotate(matrix)
# for i in range(len(matrix)):
#     print(matrix[i])