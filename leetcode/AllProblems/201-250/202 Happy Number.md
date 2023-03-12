# 202. Happy Number

使用hash表，时间复杂度和空间复杂度都是$O(N)$.这里的N代表遇到的数的个数

~~~python
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = dict()
        while n != 1:
            if n in visited :
                return False
            visited[n] = 1
            next_n = 0
            while n != 0:
                next_n += (n%10)**2
                n = n // 10
            
            n = next_n
        
        return True
~~~

根据数学推断性质，已知$D(N)$为数字N中的数字的个数
$$
D(N) = \lfloor\text{log}_{10}^N\rfloor + 1\\
\text{当}N > 1000 \text{时}:\quad D(N) * 100 < N
$$
则给定一个序列$N_0, N_1, N_2，\dots$

当$N_0 > 1000$时，有：
$$
N1 \leq 9^2\times D(N) = 81*D(N) \leq 100 * D(N) \leq N
$$
当$N_0 < 1000$时，有：
$$
N1 \leq 9^2 \times D(N) < 100 \times D(N) < 400
$$
也即无论$N_0$的值是多大，最终都会在一个范围内变化。

对于Happy num来说，如果计算得到了之前得到的数，那么就不是happy num，那么就是说存在环，而数字都是一个范围内变化的，所以就可以用floyd判圈算法即可。

*如果从同一个起点(即使这个起点不在某个环上)同时开始以不同速度前进的2个指针最终相遇，那么可以判定存在一个环，且可以求出2者相遇处所在的环的起点与长度。*

时间复杂度是$O(N)$，空间复杂度是$O(1)$

~~~python
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(n):
            next_n = 0
            while n != 0:
                n, m = divmod(n, 10)
                next_n += m**2
            return next_n
        slow,fast = n, n
        while True:
            if fast == 1:
                return True
            slow = helper(slow)
            fast = helper(helper(fast))
            if slow == fast and fast != 1:
                return False
        
        return True
~~~

