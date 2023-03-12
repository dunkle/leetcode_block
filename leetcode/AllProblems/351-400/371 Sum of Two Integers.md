使用位操作来模拟加法操作

在不考虑进位的情况下，二进制加法有：

1+1 = 0, 1+0 = 1, 0+0=0，和异或操作非常类似

而如果单独考虑是否进位有：0+1=1,1+0=1,1+1=1,0+0=0,和且操作类似

那么就可以用异或操作来表示在不考虑进位情况下的加法，用且表示两个位数之间运算是否产生进位，因为进位是要和前一个相加，所以还要左移一位。当进位为0时，得到加法结果



~~~python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        carry = 0
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # for overflow condition like
        # -1
        #  1
        return a&mask if b > mask else a
~~~

