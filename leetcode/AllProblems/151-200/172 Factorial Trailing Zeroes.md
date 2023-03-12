# 172. Factorial Trailing Zeroes

判断阶乘数中有多少个后导0

![image-20200331140355116](../../.assert/image-20200331140355116.png)

所有的后导0都是来自2*5,而2的数量一定比5多，因此只需统计5的数量即可

~~~python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
~~~

n/m得到[1,n]中能被m整除的数的个数，$n/m^2$得到[1,n]中能被$m^2$整除的个数，因此统计能被$m,m^2,m^3,\dots$整除的个数即可。