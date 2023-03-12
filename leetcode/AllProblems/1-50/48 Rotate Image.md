# 48. Rotate Image

![image-20200404003719980](../../../.assert/image-20200404003719980.png)

给定一个二维数组代表一个图像，将其顺时针旋转90度

**旋转的操作**

~~~C
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
~~~

**Python 解1**

~~~python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
~~~

**python 解2**

这里用A[::-1]来颠倒矩阵，然后用zip进行对阵反转

~~~python
class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
~~~

