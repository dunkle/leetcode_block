给定一个由01组成的矩阵，求由1组成的最大的矩阵面积。

![image-20201007152146294](../../../.assert/image-20201007152146294.png)

对于矩阵的每一行，可以统计1位置处最高的矩形大小，然后每一行将其转换为低84题，直方图的最大面积。

~~~python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        heights = [0] * (m+1)
        ans = 0
        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            stack = [-1]
            for j in range(len(heights)):
                while heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j - 1 - stack[-1]
                    ans = max(w*h, ans)
                stack.append(j)
        return ans
            
                
~~~

