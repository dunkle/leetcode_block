# 69. Sqrt(x)

求一个数的平方根的整数部分

## 二分查找

通过二分查找找到一个数mid,使得$\text{mid}^2 \leq x \leq (\text{mid}+1)^2$

~~~python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l, r = 1, x
        mid = (1+x) // 2
        while l < r:
            if mid**2 == x:
                return mid
            if (mid+1)**2 == x:
                return mid+1
            if mid**2 < x and (mid+1)**2 > x:
                return mid
            if mid**2 > x:
                r = mid
                mid = (l+r)//2
            if (mid+1)**2 < x:
                l = mid
                mid = (l+r) // 2
        return mid
~~~


## 牛顿法

找到一个数x，使得$x^2=N$，也即求方程$x^2 - N = 0$的根。则有：
$$
f(x) = x^2 - N \\
f'(x) = \frac{x_1 - x_2}{f(x_1)-f(x_2)} \\
$$
令$f(x_2)=0$解出$x_2$即可得到根:
$$
x_2 = x_1 - \frac{f(x_1)}{f'(x_1)}
$$
对于本题可以不断求解：
$$
x_2 = \frac{x_1^2 + N}{2x_1}
$$

这里还用到了不动点的思想，对于方程$f(x)=x$，不断求$f(x), f(f(x)), f(f(f(x))),\dots$，使得其值变化不大时，即可求出$f(x)=x$的解。

~~~python
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x + 1  # avoid dividing 0
        while r*r > x:
            r = int(r - (r*r - x)/(2*r))  # newton's method
        return r
~~~

