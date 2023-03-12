# 279 Perfect Square

![image-20200418155807713](../../../.assert/image-20200418155807713.png)

给定一个数，找到数量最少的完全平方数（1,4,9,16,..）使其和为n

## BFS

将n与$[1,4,..,\lfloor\sqrt{n}\rfloor^2]$相减,直到有一个值为0

~~~python
class Solution:
    def numSquares(self, n: int) -> int:
        
        times, queue = 0, [n]
        while queue:
            # print(queue)
            tmp = []
            times += 1
            for t in queue:
                c = math.floor(math.sqrt(t))
                for i in range(1, c+1):
                    if i**2 == t:
                        return times
                    else:
                        tmp.append(t-i**2)
            queue = tmp
~~~

## 动态规划

设$C[i]$为组成i所需的最小步骤则：
$$
C[i] = \text{min}(\text{min}(C[n-t^2]), i),\quad t=1,\dots\sqrt{i}
$$

~~~python
class Solution:
    def numSquares(self, n: int) -> int:
        
        cnt = [n+1] * (n+1)
        cnt[0] = 0
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                cnt[i] = min(cnt[i], cnt[i-j**2]+1)
                j += 1
        return cnt[n]
~~~

## 数学

根据[Lagrange's four-square theorem](https://en.wikipedia.org/wiki/Lagrange's_four-square_theorem)，任何一个数都是4个完全平方数（包含零）的和，所以：

1. $n<4$直接返回n
2. 穷举$[1,4,\dots,\lfloor\sqrt{n}\rfloor]^2$中能否找到组成n的数
3. 没有则返回4

~~~python
class Solution:
    def numSquares(self, n):
        if n<4:
            return n
        sqr = int(sqrt(n))+1
        pool = {i**2 for i in range(sqr)}
        test = [i**2 for i in range(sqr)]
        for i in test:
            for j in test:
                if n-i-j in pool:
                    return 3 - (i==0) - (j==0)
        return 4
~~~

