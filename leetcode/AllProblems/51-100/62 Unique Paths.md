# 62. Unique Paths

![image-20200409141536432](../../.assert/image-20200409141536432.png)

给定(m,n)的地图，求左上角到右下角的所有可能的路径。

## DP1

构造一个(m,n)的数组，从右下角开始计算，状态是当前可能的路径，状态转移方程为：
$$
C[i,j] = C[i+1, j] + C[i, j+1]
$$
最后一排和最后一列是1

时间复杂度为O(m*n)，空间复杂度为O(m\*n)

~~~python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for _ in range(m):
            grid.append([1]*n)
            
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                grid[i][j] = grid[i+1][j] + grid[i][j+1]
        # for g in grid:
        #     print(g)
        return grid[0][0]
~~~

## DP2

用两个长度为n的数组即可，一个记录当前行，一个记录前一行

时间复杂度为O(m*n)，空间复杂度为O(n)

~~~python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * n
        current = pre
        for i in range(m-1):
            current = [1]
            for j in range(1, n):
                current.append(current[j-1]+pre[j])
            pre = current
        return current[-1]
~~~

## 数学公式

因为只能向下和向右运动，因此路径只能为"右下下下右右"，也即向右和向下的组合数，共需向右(m-1)次，向下(n-1)次，因此序列长度为(m+n-2)次，所以全部结果为$C_S^{m-1} = (m+n-1)!/(m-1)!(n-1)!$

时间复杂度为O(m+n),空间复杂度为O(1)

~~~python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
~~~



