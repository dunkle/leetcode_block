# Search a 2D Matrix

![image-20200706105952562](../../../.assert/image-20200706105952562.png)

给定一个二维数组，每行是有序的，下一行第一个值比上一行第一个值大

如果从中间开始寻找，那么要搜索三个区域，而且区域之间还有重叠。可以从右上角开始搜索，左边比其小，下遍比其大。



~~~python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        rows, cols = len(matrix), len(matrix[0])
        x, y = 0, cols-1
        while True:
            if x >= rows or y < 0:
                return False
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False
~~~

