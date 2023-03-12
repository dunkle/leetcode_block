# Power of Three

![image-20200330111033689](../../.assert/image-20200330111033689.png)

给定一个数，判断是否为3的n次幂

## 循环

令n除3，直到余数不为0或n为1

~~~python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        
        if n < 1:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1
~~~

## 题目分析法

题目的输入是一个整数，大小为4byte，也即能表示的最大整数为**2147483647**，则小于它的最大的3的幂为$3^{\lfloor\text{log}MaxInt\rfloor} = 3^{\lfloor19.56\rfloor} = 3^19 = 1162261467$,该值只能被3的n次幂整除，所以只需判断该值能否被n整除即可。

~~~python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
~~~



## 数学推断

若$\text{log}_3^{n}$为整数，则n为3的n次幂。根据公式：
$$
n = 3^i \\
i = \text{log}_3^n \\
\text{log}_3^n = \frac{\text{log}_{10}^n}{\text{log}_{10}^3}
$$

~~~python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        EPSILON = 1e-10
        return (math.log(n, 3) + EPSILON) % 1 <= 2 * EPSILON
~~~

EPSILON是为了防止出现4.99999，5.000001等精度问题。