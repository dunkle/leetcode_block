统计一个数的二进制表示中1的个数。

对于无符号整数来说，可以逐个判断每一位是否为1，然后计数。时间复杂度为$O(N)$,N为位数，空间复杂度为$O(1)$

~~~python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if n & 2**i:
                count += 1
        return count
~~~
也可以直接统计数字中出现的1的个数，利用的一个Trick是n&(n-1)会将n中的最后一位的1置为0.此时时间复杂度为$O(N_1)$,$N_1$为二进制中1的个数，空间复杂度为$O(1)$

~~~python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n & (n-1)
            count += 1
        return count
~~~

关于Tricks的证明：

假设n的二进制表示为`01001100`,则(n-1)为`01001011`,n&(n-1)即为`01001000`

