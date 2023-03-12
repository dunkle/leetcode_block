# 240. Search a 2D Matrix II

![image-20200420181209348](../../../.assert/image-20200420181209348.png)

给定一个有序矩阵，矩阵每一行每一列都比前面的值大（升序），判断一个值是否在数组中

## 直接查找

从右上角的值大开始比较：

1. 如果大于则这一行必定小于target可以查看下一行
2. 如果小于则这一列必定大于target，可以查看前一列
3. 相等返回True

~~~python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            # print(row, col)
            if target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -=1
            elif target == matrix[row][col]:
                return True
        return False
   
~~~

共有N行M列，时间复杂度为O(N+M)

## 二分查找

对每一行进行二分查找，时间复杂度为O(NlogM)