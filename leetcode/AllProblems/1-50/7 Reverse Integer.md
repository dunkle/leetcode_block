# 7. Reverse Integer

![image-20200402204337251](../../../.assert/image-20200402204337251.png)

给定一个有符号整数，将其反转

首先记录符号，然后将数字转为字符串反转之后判断是否溢出，与符号相乘。

~~~python
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if  x > 0 else -1
        n = "0"
        n = int(str(sign*x)[::-1])
        return (n*sign) * (n < 2**31)
~~~

