# 70. Climbing Stairs

![image-20200329150047026](../../.assert/image-20200329150047026.png)

使用动态规划算法，将状态定义为有n阶台阶时的步骤种类，记为$C[n]$；解决这个问题可以转移为第一步为2时C[n-2]和第一步为1时C[n-1]的和。

~~~python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        t = list()
        t.append(2)
        t.append(3)
        i = 2
        while i <= n - 2:
            t.append(t[-1] + t[-2])
            i += 1
        return t[n-2]
~~~

