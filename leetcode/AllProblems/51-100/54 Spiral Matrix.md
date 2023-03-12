给定一个矩阵，返回一个列表，列表内容为顺时针旋转的值

![image-20201006154239768](../../../.assert/image-20201006154239768.png)

~~~python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        l, r, b, t = 0, len(matrix[0])-1, len(matrix)-1, 0
        result = []
        while True:
            for i in range(l, r+1):
                result.append(matrix[t][i])
            t+=1
            if t > b:
                break
            for i in range(t, b+1):
                result.append(matrix[i][r])
            r-=1
            if l > r:
                break
            for i in range(r, l-1, -1):
                result.append(matrix[b][i])
            b -= 1
            if t > b:
                break
            for i in range(b, t-1, -1):
                result.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return result
~~~

